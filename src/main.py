"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Taste profile: a late-night focused listener who prefers mellow,
    # acoustic-leaning lofi and jazz with just enough energy to stay productive.
    user_prefs = {
        "favorite_genre":       "lofi",    # primary genre preference
        "favorite_mood":        "focused", # preferred emotional atmosphere
        "target_energy":        0.42,      # calm but not completely passive
        "target_tempo_bpm":     80.0,      # slow-to-mid tempo; nothing frantic
        "target_valence":       0.62,      # slightly positive, not euphoric
        "target_danceability":  0.58,      # gentle groove is fine
        "target_acousticness":  0.78,      # strongly prefers acoustic/organic textures
        "likes_acoustic":       True,      # shorthand flag for filtering/boosting
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 44)
    print("   Top 5 Recommendations")
    print("=" * 44)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']}  —  {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Score: {score:.2f}")
        print(f"    Why: {explanation}")


if __name__ == "__main__":
    main()
