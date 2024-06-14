def selectionsort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        print('1:--')
        for j in range(i+1, n):
            if A[j] < A[position]:
                print('2:--')
                position = j
    
        temp = A[i]
        A[i] = A[position]
        A[position] = temp
        print('3:--')


A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
selectionsort(A)
print('Sorted Array:',A)


#realtime application
def selection_sort(songs):
  """
  This function sorts a list of songs based on their ratings using selection sort.

  Args:
      songs: A list of dictionaries, where each dictionary represents a song
          with keys like "title", "artist", "rating", etc.

  Returns:
      The sorted list of songs.
  """

  for i in range(len(songs) - 1):
    min_index = i
    for j in range(i + 1, len(songs)):
      if songs[j]["rating"] > songs[min_index]["rating"]:  # Sort by rating (descending)
        min_index = j

    # Swap the song with the minimum rating to its correct position
    songs[i], songs[min_index] = songs[min_index], songs[i]

  return songs

# Example usage
songs = [
  {"title": "Bohemian Rhapsody", "artist": "Queen", "rating": 5},
  {"title": "Imagine", "artist": "John Lennon", "rating": 4.8},
  {"title": "Hallelujah", "artist": "Leonard Cohen", "rating": 3.7},
  {"title": "Hotel California", "artist": "Eagles", "rating": 4.5},
]

sorted_songs = selection_sort(songs.copy())  # Avoid modifying the original list

print("Songs sorted by rating (descending):")
for song in sorted_songs:
  print(f"  - {song['title']} by {song['artist']} (Rating: {song['rating']})")
