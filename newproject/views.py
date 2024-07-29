from django.shortcuts import render
from typing import Dict
from django.http import HttpRequest

def index(request):
    return render(request, 'index.html')

def dashboard_callback(request: HttpRequest, context) -> Dict:

    bar_chart_data = {
        "labels": [
            "07/22",
            "07/23",
            "07/24",
            "07/25",
            "07/26",
            "07/27",
            "07/28"
        ],
        "datasets": [
            {
                "label": "매출",
                "backgroundColor": "rgba(255, 99, 132, 0.5)",
                "data": [
                    20372365,
                    21077579,
                    21577157,
                    25058620,
                    29522239,
                    2496161,
                    24914666
                ],
                "stack": "Stack 0"
            },
            {
                "label": "매입",
                "backgroundColor": "rgba(0, 156, 123, 0.5)",
                "data": [
                    13751566,
                    16303560,
                    31039019,
                    33621116,
                    34660119,
                    0,
                    0
                ],
                "stack": "Stack 1"
            }
        ]
    }

    bar_chart_data = "{\"labels\":[\"07/22\",\"07/23\",\"07/24\",\"07/25\",\"07/26\",\"07/27\",\"07/28\"],\"datasets\":[{\"label\":\"매출\",\"backgroundColor\":\"rgba(255,99,132,0.5)\",\"data\":[20372365,21077579,21577157,25058620,29522239,2496161,24914666],\"stack\":\"Stack0\"},{\"label\":\"매입\",\"backgroundColor\":\"rgba(0,156,123,0.5)\",\"data\":[13751566,16303560,31039019,33621116,34660119,0,0],\"stack\":\"Stack1\"}]}"
    context.update({
        "cards": [
            {
                "title": "Card 1",
                "footer": "Footer 1",
                "metric": "Label 1",
                "icon": "icon 1",
            },
            {
                "title": "Card 2",
                "footer": "Footer 2",
                "metric": "Label 2",
                "icon": "icon 2",
            },
        ],
        "table_data": {
            "headers": ["col 1", "col 2"],
            "rows": [
                ["a", "b"],
                ["c", "d"],
            ]
        },
        "bar_chart_data": bar_chart_data,
    })
    return context