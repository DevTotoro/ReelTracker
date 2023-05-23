import requests
from PIL import Image
from io import BytesIO



class MovieApi:
    # exit flags for threads
    exit_flags = {}
    
    # api key 
    api_key = '58758d128c2026c646f36ebf2c3cf444'
    
    # chosen movie and series genres with their id 
    movie_genre = {
        'Action': 28,
        'Comedy': 35,
        'Crime': 80,
        'Drama': 18,
        'Horror': 27,
        'Mystery': 9648,
        'Sci-fi': 878,
        'Thriller': 53
    }
    
    series_genre = {
        'Action & Adventure': 10759,
        'Anime': 16,
        'Comedy': 35,
        'Crime': 80,
        'Documentary': 99,
        'Drama': 18,
        'Mystery': 9648,
        'Sci-Fi & Fantasy': 10765
    }
    
    # this function takes as arguments a query, a ScrollableMoviesFrame, a start-end range and a thread id , performs 
    # a search for series by name in moviedb and adds results to scrollable frame. If exit_flag is set , returns.
    def search_series(self, query, frame, start, end, thread_id):
        url = f'https://api.themoviedb.org/3/search/tv?api_key={self.api_key}&query={query}'
        i = 0
        response = requests.get(url)
        data = response.json()

        if 'results' in data:
            results = data['results']
            exit_flag = self.exit_flags[thread_id]
            for series in results:
                # if series is in range [start,end] and exit_flag isnt set
                if i < end and i >= start and not exit_flag.isSet():
                    poster_path = series['poster_path']
                    title = series['name']
                    # Constructing the URL to the poster image
                    base_image_url = 'https://image.tmdb.org/t/p/w154'  # You can change the image size if desired
                    image_url = f'{base_image_url}{poster_path}' if poster_path else None

                    if image_url:
                        image_response = requests.get(image_url)
                        image = Image.open(BytesIO(image_response.content))
                        if frame:
                            frame.add_item(title, image)
                # if i >= end or exit flag is set
                elif i>= end or exit_flag.isSet():
                    return
                i += 1
            
    
    # this function takes as arguments a query, a ScrollableMoviesFrame, a start-end range and a thread id , performs 
    # a search for movies by name in moviedb and adds results to scrollable frame. If exit_flag is set , returns.
    def search_movies(self, query, frame, start, end, thread_id):
        url = f'https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={query}'
        i = 0
        # search query and jsonify
        response = requests.get(url)
        data = response.json()

        if 'results' in data:
            results = data['results']
            exit_flag = self.exit_flags[thread_id]
            for movie in results:
                # if movie is in range [start,end] and exit_flag isnt set
                if i < end and i >= start and not exit_flag.isSet():
                    poster_path = movie['poster_path']
                    title = movie['title']
                    # Constructing the URL to the poster image
                    base_image_url = 'https://image.tmdb.org/t/p/w154'  
                    image_url = f'{base_image_url}{poster_path}' if poster_path else None

                    if image_url:
                        # download image
                        image_response = requests.get(image_url)
                        image = Image.open(BytesIO(image_response.content))
                        if frame:
                            # add image to frame
                            frame.add_item(title, image)
                # if i >= end or exit flag is set
                elif i>= end or exit_flag.isSet():
                    return
                i += 1
        return

    # same logic as search_movie_by_genre
    def search_series_by_genre(self, genre_id, frame, start, end):
        page = int((end-1)/14) + 1
        start -= (page-1)*14 
        end -= (page-1)*14
        
        url = f'https://api.themoviedb.org/3/discover/tv?api_key={self.api_key}&with_genres={genre_id}&page={page}'

        response = requests.get(url)
        data = response.json()
        i=0
        
        if 'results' in data:
            results = data['results']
            for series in results:
                if i < end and i >= start:
                    poster_path = series['poster_path']
                    title = series['name']
                    # Constructing the URL to the poster image
                    base_image_url = 'https://image.tmdb.org/t/p/w154'  # You can change the image size if desired
                    image_url = f'{base_image_url}{poster_path}' if poster_path else None

                    if image_url:
                        image_response = requests.get(image_url)
                        image = Image.open(BytesIO(image_response.content))
                        if frame:
                            frame.add_item(title, image)
                elif i>=end:
                    return
                i += 1
        return
    
    
    def search_movies_by_genre(self, genre_id, frame, start, end):
        # calculate the page to look up for movies. Every page is 20 movies . So every 20 movies we have to change a page. 
        page = int((end-1)/14) + 1
        # after choosing a page we have to adjust start and end
        start -= (page-1)*14 
        end -= (page-1)*14 
        
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&with_genres={genre_id}&page={page}'

        # get response and jsonify
        response = requests.get(url)
        data = response.json()
        
        # counter
        i=0
        
        if 'results' in data:
            results = data['results']
            # for every movie in results
            for movie in results:
                if i < end and i >= start:
                    poster_path = movie['poster_path']
                    # Constructing the URL to the poster image
                    base_image_url = 'https://image.tmdb.org/t/p/w154' 
                    image_url = f'{base_image_url}{poster_path}' if poster_path else None

                    # create image and add it to frame
                    if image_url:
                        image_response = requests.get(image_url)
                        image = Image.open(BytesIO(image_response.content))
                        if frame:
                            frame.add_item('',image)
                # if we surpassed the end return
                elif i>=end:  
                    return
                i += 1
        return
        