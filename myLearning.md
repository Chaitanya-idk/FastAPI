                            /*          Fast API            */
                    
Day-1 ; 3rd Aug ; 01:10 AM

FastAPI is a cutting-edge, fast web framework for creating APIs using common Python type
hints. It is renowned for its ease of use, speed, and automatic documentation, and it is
used to create RESTful APIs rapidly and effectively.

Pro's :

1. ASGI-based Framework
    (*)FastAPI is built on ASGI (Asynchronous Server Gateway Interface), which supports     asynchronous programming and is faster than older WSGI-based frameworks like Flask or Django.

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
    