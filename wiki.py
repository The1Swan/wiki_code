from queue import Queue
import wikipediaapi
import time

#setup stuff
user_agent = "wiki_code (isabella.ann.swan@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

# function to return list of links
def fetch_links(page):
    links_list =[]
    links = page.links

    for title in links.keys():
        links_list.append(title)
    
    return links_list

def wikipedia_game_solver(start_page, target_page):
    print("working on it.....")
    start_time = time.time()

    queue = Queue()
    visted = set()
    parent = {}

    queue.put(start_page.title)
    visted.add(start_page.title)

    while not queue.empty():
        current_page_title = queue.get()
        if current_page_title == target_page.title:
            break

        current_page = wiki.page(current_page_title)
        links = fetch_links(current_page)

        for link in links:
            if link not in visted:
                queue.put(link)
                visted.add(link)
                parent[link] = current_page_title

    path = []
    page_title = target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_title = parent[page_title]

    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print("this algoritn took", end_time - start_time, "seconds.")
    return path

# start and end pages for our wikipedia game solver
start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("World War II")
path = wikipedia_game_solver(start_page, target_page)
print(path)