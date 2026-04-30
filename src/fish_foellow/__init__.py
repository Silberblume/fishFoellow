# placeholder
import git


# Set version
repo = git.Repo('.', search_parent_directories=True)
repo.config_reader()



head = repo.head.commit.__str__()
for tag in repo.tags:
    if tag.commit.__str__() == head:
        __version__ = tag.name.__str__()
        print("got")
#__version__ = "tags"

print('done')