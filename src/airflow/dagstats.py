from typing import Any, Callable, Dict, List, Optional, Union

import mcp.types as types
from airflow_client.client.api.dag_stats_api import DagStatsApi

from src.airflow.airflow_client import api_client

dag_stats_api = DagStatsApi(api_client)


def get_all_functions() -> list[tuple[Callable, str, str, bool]]:
    """Return list of (function, name, description, is_read_only) tuples for registration."""
    return [
        (get_dag_stats, "get_dag_stats", "Get DAG stats for the given list of IDs", True),
    ]


async def get_dag_stats(
    dag_ids: List[str],
) -> List[Union[types.TextContent, types.ImageContent, types.EmbeddedResource]]:
    # Build parameters dictionary
    kwargs: Dict[str, Any] = {}
    kwargs["dag_ids"] = ','.join(dag_ids)

    response = dag_stats_api.get_dag_stats(**kwargs)
    return [types.TextContent(type="text", text=str(response.to_dict()))]
