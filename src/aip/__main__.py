"""AIP CLI entry point — run the framework on a startup scenario."""

from __future__ import annotations

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from aip.config import settings
from aip.graph import compile_graph
from aip.models.startup import StartupProfile
from aip.state import initial_state

console = Console()


def load_scenario(path: str) -> StartupProfile:
    """Load a startup scenario from JSON."""
    scenario_path = Path(path)
    if not scenario_path.exists():
        # Check in scenarios/ directory
        scenario_path = settings.output_dir.parent / "scenarios" / path
        if not scenario_path.exists():
            console.print(f"[red]Scenario not found: {path}[/red]")
            sys.exit(1)

    data = json.loads(scenario_path.read_text(encoding="utf-8"))
    return StartupProfile.model_validate(data)


def display_startup(profile: StartupProfile) -> None:
    """Display startup profile in a rich table."""
    table = Table(title=f"Startup: {profile.name}", show_header=True)
    table.add_column("Dimension", style="cyan")
    table.add_column("Value", style="white")

    table.add_row("Industry", profile.industry)
    table.add_row("Stage", profile.stage)
    table.add_row("Employees", str(profile.employees))
    table.add_row("IT-Score", f"{profile.genome.it_score:.2f} / 5.00")
    table.add_row("Weakest Dimension", profile.genome.weakest_dimension)
    table.add_row("Data Maturity", f"Level {profile.genome.data_maturity_level.value}")
    table.add_row("Data Sources", ", ".join(profile.available_data))

    console.print(table)


def display_phase_a_results(state: dict) -> None:
    """Display Phase A results."""
    phase_a = state.get("phase_a")
    if not phase_a:
        console.print("[yellow]Phase A did not produce output.[/yellow]")
        return

    # Innovation Gaps
    console.print(Panel("[bold]Phase A: ERKENNEN — Results[/bold]", style="green"))

    console.print(f"\n[bold]Exploitation/Exploration:[/bold] {phase_a.exploitation_exploration_ratio}")

    console.print("\n[bold]Market Trends:[/bold]")
    for trend in phase_a.market_trends[:5]:
        console.print(f"  - {trend}")

    console.print("\n[bold]Innovation Gaps:[/bold]")
    gap_table = Table(show_header=True)
    gap_table.add_column("#", style="dim")
    gap_table.add_column("Gap", style="cyan")
    gap_table.add_column("Severity", style="red")
    gap_table.add_column("BMC Block")

    for i, gap in enumerate(phase_a.innovation_gaps, 1):
        gap_table.add_row(
            str(i),
            gap.title,
            gap.severity,
            gap.source_block,
        )
    console.print(gap_table)

    # Gate Decision
    gate = phase_a.gate_decision
    if gate:
        style = "green" if gate.decision == "go" else "yellow" if gate.decision == "iterate" else "red"
        console.print(f"\n[bold]Gate A→B:[/bold] [{style}]{gate.decision.upper()}[/{style}]")
        console.print(f"  Rationale: {gate.rationale}")
        console.print(f"  Confidence: {gate.confidence:.0%}")

        if gate.dissent_signals:
            console.print(f"\n[bold yellow]Dissent Signals ({len(gate.dissent_signals)}):[/bold yellow]")
            for d in gate.dissent_signals:
                console.print(f"  [{d.divergence_score:.0%} divergence] {d.topic}")
                console.print(f"    Innovation potential: {d.innovation_potential}")

    # Dissent signals from state
    all_dissent = state.get("dissent_signals", [])
    if all_dissent:
        console.print(f"\n[bold yellow]Total Dissent Signals: {len(all_dissent)}[/bold yellow]")


async def run_aip(scenario_path: str) -> None:
    """Run the AIP framework on a scenario."""
    console.print(Panel("[bold blue]AIP — Agentic Innovation Process[/bold blue]", subtitle="v0.1.0"))

    # Load scenario
    profile = load_scenario(scenario_path)
    display_startup(profile)

    # Validate API key
    if not settings.anthropic_api_key:
        console.print("[red]Error: AIP_ANTHROPIC_API_KEY not set. Create a .env file.[/red]")
        sys.exit(1)

    # Build and run graph
    console.print("\n[bold]Starting AIP cycle...[/bold]\n")
    graph = compile_graph()

    state = initial_state(profile)

    # Run the graph
    config = {"configurable": {"thread_id": f"aip-{profile.name}-{datetime.now().isoformat()}"}}

    console.print("[dim]Running Phase A: ERKENNEN...[/dim]")
    result = await graph.ainvoke(state, config=config)

    # Display results
    display_phase_a_results(result)

    # Save output
    output_dir = settings.output_dir / profile.name.lower().replace(" ", "_")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"phase_a_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    phase_a = result.get("phase_a")
    if phase_a:
        output_data = phase_a.model_dump() if hasattr(phase_a, "model_dump") else phase_a
        output_file.write_text(
            json.dumps(output_data, indent=2, default=str, ensure_ascii=False),
            encoding="utf-8",
        )
        console.print(f"\n[green]Output saved to {output_file}[/green]")


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        console.print("Usage: python -m aip <scenario.json>")
        console.print("Example: python -m aip scenarios/saas_stagnation.json")
        sys.exit(1)

    asyncio.run(run_aip(sys.argv[1]))


if __name__ == "__main__":
    main()
