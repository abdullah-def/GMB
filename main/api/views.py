from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.

from datetime import date, timedelta


def get_chart_reviews_stars(_request):

    chart = {
        'color':[
            '#85a9ff', #primary
            '#adc5ff', #primary-200
            '#0097eb', #info-500
            '#005585',
            '#003cc7',
        ],
        'tooltip':{
            'trigger':"item",
            'padding':[7,10],
            # 'backgroundColor':'#222834',
            'borderColor':'#373e53',
            # 'textStyle':{'color':'dark'},
            'borderWidth':1,
            'transitionDuration':0,
        },
        'legend':{
            'show':False
        },
        'series':[
            {
                'name':"Stars Rate",
                'type':"pie",
                'sampling': 'average',
                'large': True,
                'symbol':"none",
                'radius':["100%","87%"],
                'avoidLabelOverlap':False,
                'emphasis':{
                    'label': {
                        'show': True,
                        'fontSize': 23,
                        # 'fontWeight': 'bold',
                        'color':'dark'
                        },
                    'scale':False,
                    'itemStyle':{'color':"inherit"}
                },
                'itemStyle':{
                    'borderWidth':2,
                    # 'borderColor':'#0f111a'
                },'label':{
                    'show':False,
                    'position':"center",
                    # 'formatter':"{a}",
                    # 'fontSize':23,
                    # 'color':'dark'
                },

                'data':[
                    
                    {'value':80,'name':"5 Stars"},
                    {'value':6,'name':"4 Stars"},
                    {'value':4,'name':"3 Stars"},
                    {'value':7,'name':"2 Stars"},
                    {'value':3,'name':"1 Stars"}
                ]
            },
            
        ],
        'grid':{'containLabel':True}
                
                
    }

    return JsonResponse(chart)

def get_chart_reviews_response(_request):
    last_week = []
    today = date.today()

    for i in range(7):
        day = today - timedelta(days=i)
        iso = day.strftime("%b %d")
        last_week.append(iso)

    reviews=[5,6,2,8,0,3,10]
    reviews_response=[4,3,2,6,0,2,4]

    chart = {
        'tooltip': {
            'show':True,
            'trigger': "axis",
            'padding':10,
            # 'backgroundColor':'#222834',
            'showContent': True,
            # 'borderColor':'#373e53',
            'textStyle':{'color':"inherit"},
            'borderWidth':1,
            'transitionDuration':0,
            'axisPointer':{'type':"none"}
        },
        'xAxis':[
            {
                'type':"category",
                'data': last_week,
                'show': True,
                'boundaryGap':False,
                'axisLine':{
                    'show':True,
                    'lineStyle':{'color':'#31374a'}
                },
                'axisTick':{'show':False},
                'axisLabel':{'formatter':last_week[0],'showMinLabel':True,'showMaxLabel':False,'color':'#949db5', 'align':"left",'interval':5,'fontFamily':"Nunito Sans",'fontWeight':600,'fontSize':12.8}

            },
            {'type':"category",'position':"bottom",'show':True,'data':last_week,'axisLabel':{'formatter':last_week[-1],'interval':130,'showMaxLabel':True,'showMinLabel':False,'color':'#949db5','align':"right",'fontFamily':"Nunito Sans",'fontWeight':600,'fontSize':12.8},
             'axisLine':{'show':False},'axisTick':{'show':False},'splitLine':{'show':False},'boundaryGap':False}

        ],
        'yAxis':[
            {
                'show':False,'type':"value",'boundaryGap':False

            }
        ],
        'series':[
            {
                'type':"line",'data':reviews, 'name': 'Reviews','sampling': 'average',
                'large': True,'stack': 'Total','showSymbol':False,'symbol':"circle",'lineStyle':{'width':2,'color':'31374a'},'emphasis':{'lineStyle':{'color':'31374a'}}
            },
            {
                'type':"line",'data':reviews_response,'name': 'Reviews Response','sampling': 'average',
                'large': True, 'symbol':"none",'stack': 'Total','lineStyle':{'width':2,'color':'#85a9ff'},'showSymbol':False,'symbol':"circle"
            }
        ],
        'grid':{'left':0,'right':0,'top':5,'bottom':20}
    }
    return JsonResponse(chart)

def get_chart_reviews_response_nun(_request):
    
    chart = {
        'tooltip':{
            'trigger':"item",
            'padding':[7,10],
            # 'backgroundColor':'#85a9ff',
            # 'borderColor':'#373e53',
            # 'textStyle':{'color':'dark'},
            'borderWidth':1,
        },
        'legend':{'show':False},
        'series':[
            {
                'type':"gauge",
                'center':["50%","60%"],
                'name':"Paying customer",
                'startAngle':180,
                'endAngle':0,
                'min':0,
                'max':100,
                'splitNumber':12,
                'itemStyle':{'color':'#85a9ff'},
                'progress':{
                    'show':True,
                    'roundCap':True,
                    'width':12,
                    'itemStyle':{'shadowBlur':0,'shadowColor':"#0000"}
                },
                'pointer':{'show':False},
                'axisLine':{
                    'roundCap':True,
                    'lineStyle':{'width':12,'color':[[1,'#525b75']]}
                },'axisTick':{'show':False},
                'splitLine':{'show':False},
                'axisLabel':{'show':False},
                'title':{'show':False},
                'detail':{'show':False},
                'data':[{'value':90}]                                                                                                                                                     
            }
        ]

    }
    
    return JsonResponse(chart)

def get_chart_reviews_total(_request):
    last_week = []
    today = date.today()

    for i in range(7):
        day = today - timedelta(days=i)
        iso = day.strftime("%b %d")
        last_week.append(iso)

    reviews=[5,6,2,8,0,3,10]

    chart = {
        'color':"#85a9ff",
        'tooltip': {
            'show':True,
            'trigger': "item",
            'padding':10,
            'borderColor':'#373e53',
            'textStyle':{'color':"dark"},
            'borderWidth':1,
            'transitionDuration':0,
            # 'formatter':last_week[0]

        },
        'xAxis':[
            {
                'type':"category",
                'data': last_week,
                'show': True,
                'boundaryGap':False,
                'axisLine':{
                    'show':True,
                    'lineStyle':{'color':'#31374a'}
                },
                'axisTick':{'show':True},
                'axisLabel':{'formatter':last_week[0],'interval':6,'showMinLabel':True,'showMaxLabel':True,'color':'#949db5'}

            }
        ],
        'yAxis':[
            {
                'show':False,'type':"value",'boundaryGap':True
            }
        ],
        'series':[
            {
                'type':"bar",'barWidth':"5px",'data':reviews,'showBackground':False,'symbol':"none",'itemStyle':{'borderRadius':10}, 'backgroundStyle':{'borderRadius':10,'color':'#1d2332'}
            },
            
        ],
        'grid':{'right':10,'left':10,'bottom':0,'top':0}
    }


    return JsonResponse(chart)



def get_chart_reviews(_request):
    last_week = []
    today = date.today()

    for i in range(7):
        day = today - timedelta(days=i)
        iso = day.strftime("%b %d")
        last_week.append(iso)

    reviews=[5,6,2,8,0,3,10]
    chart = {
       
        'grid': {
            'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
        },
        'tooltip': {
            'show':True,
            'trigger': "axis",
            'axisPointer':{'type':"none"}

        },
        'xAxis':[
            {
                'type':"category",
                'data': last_week,

                'splitNumber': 15,
                'splitLine': {
                    'show':True,
                    # 'interval':0,
                    'lineStyle': {
                        'color': ["#525b75"],
                       
                    },
                },
                
                
            }
        ],
        'yAxis':[
            {
                'type':"value",
                'splitLine': {
                    'show':False,
                    'lineStyle': {
                            'color': ["#525b75"],

                    },

                }
            }
        ],
        'series':[
            {
                'data':reviews,
                'type': 'line',
                'symbol':"none",'sampling': 'average', 'large': True,
            }
        ]

    }

    return JsonResponse(chart)


def get_chart_reviews_dash(_request):
    last_week = []
    today = date.today()

    for i in range(7):
        day = today - timedelta(days=i)
        iso = day.strftime("%b %d")
        last_week.append(iso)

    reviews=[5,6,2,8,0,3,10]
    reviews2=[20,8,2,12,8,3,4]

    chart = {
       
        'grid': {
            'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
        },
        'tooltip': {
            'show':True,
            'trigger': "axis",
            'axisPointer':{'type':"none"}

        },
        'xAxis':[
            {
                'type':"category",
                'data': last_week,

                'splitNumber': 15,
                'splitLine': {
                    'show':True,
                    # 'interval':0,
                    'lineStyle': {
                        'color': ["#525b75"],
                       
                    },
                },
                
                
            }
        ],
        'yAxis':[
            {
                'type':"value",
                'splitLine': {
                    'show':False,
                    'lineStyle': {
                            'color': ["#525b75"],

                    },

                }
            }
        ],
        'series':[
            {
                'type':"line",'data':reviews, 'name': 'Oneway Lebanese Bakery','sampling': 'average',
                'large': True,'stack': 'Total','showSymbol':False,'symbol':"circle",'lineStyle':{'width':2,'color':'31374a'},'emphasis':{'lineStyle':{'color':'31374a'}}
            },
            {
                'type':"line",'data':reviews2,'name': 'Automaxed','sampling': 'average',
                'large': True, 'symbol':"none",'stack': 'Total','lineStyle':{'width':2,'color':'#85a9ff'},'showSymbol':False,'symbol':"circle"
            }
        ]

    }

    return JsonResponse(chart)
def get_chart_reviews_dash_p(_request, year):
    if year ==7:
        return get_chart_reviews_dash(_request)
    
    elif year == 14:
        last_week = []
        today = date.today()

        for i in range(14):
            day = today - timedelta(days=i)
            iso = day.strftime("%b %d")
            last_week.append(iso)

        reviews=[5,6,2,8,0,3,10,5,6,2,8,0,3,10]
        reviews2=[6,7,1,10,25,3,5,8,9,4,20,1,0,10]

        chart = {
        
            'grid': {
                'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
            },
            'tooltip': {
                'show':True,
                'trigger': "axis",
                'axisPointer':{'type':"none"}

            },
            'xAxis':[
                {
                    'type':"category",
                    'data': last_week,

                    'splitNumber': 15,
                    'splitLine': {
                        'show':True,
                        # 'interval':0,
                        'lineStyle': {
                            'color': ["#525b75"],
                        
                        },
                    },
                    
                    
                }
            ],
            'yAxis':[
                {
                    'type':"value",
                    'splitLine': {
                        'show':False,
                        'lineStyle': {
                                'color': ["#525b75"],

                        },

                    }
                }
            ],
            'series':[
                {
                    'type':"line",'data':reviews, 'name': 'Oneway Lebanese Bakery','sampling': 'average',
                    'large': True,'stack': 'Total','showSymbol':False,'symbol':"circle",'lineStyle':{'width':2,'color':'31374a'},'emphasis':{'lineStyle':{'color':'31374a'}}
                },
                {
                    'type':"line",'data':reviews2,'name': 'Automaxed','sampling': 'average',
                    'large': True, 'symbol':"none",'stack': 'Total','lineStyle':{'width':2,'color':'#85a9ff'},'showSymbol':False,'symbol':"circle"
                }
            ]

        }

        return JsonResponse(chart)
    
    elif year == 30:
        
        last_week = []
        today = date.today()

        for i in range(30):
            day = today - timedelta(days=i)
            iso = day.strftime("%b %d")
            last_week.append(iso)

        reviews=[5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60]
        reviews2=[10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60,5,6,2,8,0,3,10,5,6,2,8,0,3]

        chart = {
        
            'grid': {
                'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
            },
            'tooltip': {
                'show':True,
                'trigger': "axis",
                'axisPointer':{'type':"none"}

            },
            'xAxis':[
                {
                    'type':"category",
                    'data': last_week,

                    'splitNumber': 15,
                    'splitLine': {
                        'show':True,
                        # 'interval':0,
                        'lineStyle': {
                            'color': ["#525b75"],
                        
                        },
                    },
                    
                    
                }
            ],
            'yAxis':[
                {
                    'type':"value",
                    'splitLine': {
                        'show':False,
                        'lineStyle': {
                                'color': ["#525b75"],

                        },

                    }
                }
            ],
            'series':[
                {
                    'type':"line",'data':reviews, 'name': 'Oneway Lebanese Bakery','sampling': 'average',
                    'large': True,'stack': 'Total','showSymbol':False,'symbol':"circle",'lineStyle':{'width':2,'color':'31374a'},'emphasis':{'lineStyle':{'color':'31374a'}}
                },
                {
                    'type':"line",'data':reviews2,'name': 'Automaxed','sampling': 'average',
                    'large': True, 'symbol':"none",'stack': 'Total','lineStyle':{'width':2,'color':'#85a9ff'},'showSymbol':False,'symbol':"circle"
                }
            ]

        }

        return JsonResponse(chart)
    
    elif year == 2:
        
        last_week = []
        today = date.today()

        for i in range(60):
            day = today - timedelta(days=i)
            iso = day.strftime("%b %d")
            last_week.append(iso)

        reviews=[5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60]
        reviews2=[60,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30]

        chart = {
        
            'grid': {
                'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
            },
            'tooltip': {
                'show':True,
                'trigger': "axis",
                'axisPointer':{'type':"none"}

            },
            'xAxis':[
                {
                    'type':"category",
                    'data': last_week,

                    'splitNumber': 15,
                    'splitLine': {
                        'show':True,
                        # 'interval':0,
                        'lineStyle': {
                            'color': ["#525b75"],
                        
                        },
                    },
                    
                    
                }
            ],
            'yAxis':[
                {
                    'type':"value",
                    'splitLine': {
                        'show':False,
                        'lineStyle': {
                                'color': ["#525b75"],

                        },

                    }
                }
            ],
            'series':[
                {
                    'type':"line",'data':reviews, 'name': 'Oneway Lebanese Bakery','sampling': 'average',
                    'large': True,'stack': 'Total','showSymbol':False,'symbol':"circle",'lineStyle':{'width':2,'color':'31374a'},'emphasis':{'lineStyle':{'color':'31374a'}}
                },
                {
                    'type':"line",'data':reviews2,'name': 'Automaxed','sampling': 'average',
                    'large': True, 'symbol':"none",'stack': 'Total','lineStyle':{'width':2,'color':'#85a9ff'},'showSymbol':False,'symbol':"circle"
                }
            ]

        }

        return JsonResponse(chart)
    
    elif year == 3:
        last_week = []
        today = date.today()

        for i in range(90):
            day = today - timedelta(days=i)
            iso = day.strftime("%b %d")
            last_week.append(iso)

        reviews=[5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,25,5,6,2,8,0,3,10,5,6,2,5,6,2,8,0,3,10,5,6,2,5,6,2,8,0,3,10,5,6,2]
        reviews2=[8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,25,5,6,2,8,0,3,10,5,6,2,5,6,2,8,0,3,10,5,6,2,5,6,2,8,0,3,10,5,6,2,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60,5,6,2,8,0,3,10,5,6,2]

        chart = {
        
            'grid': {
                'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
            },
            'tooltip': {
                'show':True,
                'trigger': "axis",
                'axisPointer':{'type':"none"}

            },
            'xAxis':[
                {
                    'type':"category",
                    'data': last_week,

                    'splitNumber': 15,
                    'splitLine': {
                        'show':True,
                        # 'interval':0,
                        'lineStyle': {
                            'color': ["#525b75"],
                        
                        },
                    },
                    
                    
                }
            ],
            'yAxis':[
                {
                    'type':"value",
                    'splitLine': {
                        'show':False,
                        'lineStyle': {
                                'color': ["#525b75"],

                        },

                    }
                }
            ],
            'series':[
                {
                    'type':"line",'data':reviews, 'name': 'Oneway Lebanese Bakery','sampling': 'average',
                    'large': True,'stack': 'Total','showSymbol':False,'symbol':"circle",'lineStyle':{'width':2,'color':'31374a'},'emphasis':{'lineStyle':{'color':'31374a'}}
                },
                {
                    'type':"line",'data':reviews2,'name': 'Automaxed','sampling': 'average',
                    'large': True, 'symbol':"none",'stack': 'Total','lineStyle':{'width':2,'color':'#85a9ff'},'showSymbol':False,'symbol':"circle"
                }
            ]

        }

        return JsonResponse(chart)
    
    else :
        return JsonResponse({})
    

def get_chart_reviews_P(_request, year):
    if year ==7:
        return get_chart_reviews(_request)
    
    elif year == 14:
        last_week = []
        today = date.today()

        for i in range(14):
            day = today - timedelta(days=i)
            iso = day.strftime("%b %d")
            last_week.append(iso)

        reviews=[5,6,2,8,0,3,10,5,6,2,8,0,3,10]
        chart = {
        
            'grid': {
                'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
            },
            'tooltip': {
                'show':True,
                'trigger': "axis",
                'axisPointer':{'type':"none"}

            },
            'xAxis':[
                {
                    'type':"category",
                    'data': last_week,

                    'splitNumber': 15,
                    'splitLine': {
                        'show':True,
                        # 'interval':0,
                        'lineStyle': {
                            'color': ["#525b75"],
                        
                        },
                    },
                    
                    
                }
            ],
            'yAxis':[
                {
                    'type':"value",
                    'splitLine': {
                        'show':False,
                        'lineStyle': {
                                'color': ["#525b75"],

                        },

                    }
                }
            ],
            'series':[
                {
                    'data':reviews,
                    'type': 'line',
                    
                }
            ]

        }

        return JsonResponse(chart)
    elif year == 30:
        last_week = []
        today = date.today()

        for i in range(30):
            day = today - timedelta(days=i)
            iso = day.strftime("%b %d")
            last_week.append(iso)

        reviews=[5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60]
        chart = {
        
            'grid': {
                'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
            },
            'tooltip': {
                'show':True,
                'trigger': "axis",
                'axisPointer':{'type':"none"}

            },
            'xAxis':[
                {
                    'type':"category",
                    'data': last_week,

                    'splitNumber': 15,
                    'splitLine': {
                        'show':True,
                        # 'interval':0,
                        'lineStyle': {
                            'color': ["#525b75"],
                        
                        },
                    },
                    
                    
                }
            ],
            'yAxis':[
                {
                    'type':"value",
                    'splitLine': {
                        'show':False,
                        'lineStyle': {
                                'color': ["#525b75"],

                        },

                    }
                }
            ],
            'series':[
                {
                    'data':reviews,
                    'type': 'line',
                    
                }
            ]

        }

        return JsonResponse(chart)
    
    elif year == 2:
        last_week = []
        today = date.today()

        for i in range(60):
            day = today - timedelta(days=i)
            iso = day.strftime("%b %d")
            last_week.append(iso)

        reviews=[5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60]
        chart = {
        
            'grid': {
                'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
            },
            'tooltip': {
                'show':True,
                'trigger': "axis",
                'axisPointer':{'type':"none"}

            },
            'xAxis':[
                {
                    'type':"category",
                    'data': last_week,

                    'splitNumber': 15,
                    'splitLine': {
                        'show':True,
                        # 'interval':0,
                        'lineStyle': {
                            'color': ["#525b75"],
                        
                        },
                    },
                    
                    
                }
            ],
            'yAxis':[
                {
                    'type':"value",
                    'splitLine': {
                        'show':False,
                        'lineStyle': {
                                'color': ["#525b75"],

                        },

                    }
                }
            ],
            'series':[
                {
                    'data':reviews,
                    'type': 'line',
                    
                }
            ]

        }

        return JsonResponse(chart)
    
    elif year == 3:
        last_week = []
        today = date.today()

        for i in range(90):
            day = today - timedelta(days=i)
            iso = day.strftime("%b %d")
            last_week.append(iso)

        reviews=[5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,60,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,5,6,2,8,0,3,10,30,25,5,6,2,8,0,3,10,5,6,2,5,6,2,8,0,3,10,5,6,2,5,6,2,8,0,3,10,5,6,2]
        chart = {
        
            'grid': {
                'right':2,'left':5,'bottom':"20px",'top':"2%",'containLabel':True
            },
            'tooltip': {
                'show':True,
                'trigger': "axis",
                'axisPointer':{'type':"none"}

            },
            'xAxis':[
                {
                    'type':"category",
                    'data': last_week,

                    'splitNumber': 15,
                    'splitLine': {
                        'show':True,
                        # 'interval':0,
                        'lineStyle': {
                            'color': ["#525b75"],
                        
                        },
                    },
                    
                    
                }
            ],
            'yAxis':[
                {
                    'type':"value",
                    'splitLine': {
                        'show':False,
                        'lineStyle': {
                                'color': ["#525b75"],

                        },

                    }
                }
            ],
            'series':[
                {
                    'data':reviews,
                    'type': 'line',
                    
                }
            ]

        }

        return JsonResponse(chart)
    
    else :
        return JsonResponse({})