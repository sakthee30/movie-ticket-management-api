import os
from openai import OpenAI, RateLimitError

def generate_movie_recommendations(watched_movies: list) -> list:

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        formatted_movies = "\n".join(
            [f"- {movie['title']} ({movie['genre']})" for movie in watched_movies]
        )

        prompt = f"""
        A user has previously watched the following movies:

        {formatted_movies}

        Based on their interests, recommend 5 new movies.
        Return only movie names as a JSON list.
        Example format:
        ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"]
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a movie recommendation assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except RateLimitError:
        # 🔥 Fallback if quota exceeded
        return [
            "The Dark Knight",
            "Interstellar",
            "Mad Max: Fury Road",
            "Edge of Tomorrow",
            "The Prestige"
        ]

    except Exception as e:
        return {"error": str(e)}