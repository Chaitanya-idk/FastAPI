                            /*          Fast API            */
                    
Day-1 ; 3rd Aug ; 01:10 AM


                                  # What is an API ?

An API (Application Programming Interface) is a structured way for one software application to communicate with another. It defines a set of rules or endpoints that allow applications to send or receive data without needing to know how the other system works internally.




A high-level conceptual diagram:

                    +----------------------+
                    |   Client (Frontend)  |
                    |  (Browser, Mobile)   |
                    +----------+-----------+
                               |
                               |   HTTP Request
                               v
                    +----------+-----------+
                    |         API          |   <-- Acts as a bridge/interface
                    | (Set of Endpoints &  |
                    |   Communication Rules)|
                    +----------+-----------+
                               |
                               |   Internal Function Calls / Data Access
                               v
                    +----------+-----------+
                    |   Server (Backend)   |
                    |  Business Logic / DB |
                    +----------------------+




                                    What is FAST API ?

FastAPI is a cutting-edge, fast web framework for creating APIs using common Python type
hints. It is renowned for its ease of use, speed, and automatic documentation, and it is
used to create RESTful APIs rapidly and effectively.

Pro's :

1. ASGI-based Framework
    (*)FastAPI is built on ASGI (Asynchronous Server Gateway Interface), which supports     
    asynchronous programming and is faster than older WSGI-based frameworks like Flask or Django.

    (*)This enables non-blocking I/O operations, making it suitable for modern web apps and microservices.

2. Type Hints & Pydantic
    (*)FastAPI uses Python type hints and the Pydantic library for data validation.

    (*)This allows you to define the expected structure of requests and responses using standard Python classes.

    sample code
    {
    from pydantic import BaseModel
    class Item(BaseModel):
        name: str
        price: float
    }

3. Automatic Documentation
    (*)FastAPI auto-generates API documentation using Swagger UI and ReDoc.

    (*)You get a clean, interactive UI for testing your endpoints without writing extra code.

4. Declarative Routing

    sample{
        from fastapi import FastAPI
        app = FastAPI()
        @app.get("/items/{item_id}")
        def read_item(item_id: int):
            return {"item_id": item_id}
    }

6. High Performance

    (*) FastAPI is comparable to NodeJS and Go in terms of speed, thanks to async support and optimizations using Starlette (for web handling) and Pydantic (for validation).





Problem Statement:

    We know that now a days, the AI and ML models are increasing exponentially. It is very important for us CS student to keep up with
    such fast changing technology and new concepts. Basic functionality of any AI is a small null Hypothesis that the future depends on the past
    data. we can take any example of AI or prediction, we consider that this future can be predicted on the basis of past data.

    AI - It is a concept of mimic-ing human intelligence.
        As humans did we audomantically inherit the information of how to walk ? how to write ? how to play a game ?
        No ! we learn things just by our past experiences.
        Consider playing a tik-tac-toe game, Initially you have zero knowledge about the game.You are offered a chance and you draw 
        a cross at a random place, you observe the opponent's move and their strategry of how they manage to get 3 continuos pattern.
        You understand the rules for every failed game you played.
        This process of learning from mistakes and understanding is what AI uses to improve itself.

    Then where does ML come into play ?

    Now we have a set of data consider a plot size vs price range in a given set of years.
    can we observe some pattern in those increasing or decreasing prices ???
    //This is sample random data not actual observations
    YEAR        PLOT(Sqft)        PRICE(Lakh) 
    1990        100               1.5
    2000        95                2.4
    2010        82                1.7
    2020        50                1.5                 

    Can we use mathematics and plot these ranges on a graph and draw a generelized line to find some pattern??

    Yes ! we can plot these on a (x,y) graph and use the line equation to predict prices of future prices or sqft according
    to prices.

    These methods are computationally hard to perform so we use Python to handle these data, clean them , perform appropriate
    ML requirement analysis and handle the future of that particular data. 
    This method of predicting 