from git import Repo


def main():
    repo = Repo(".")
    assert not repo.bare
    
    # get the latest state
    # exit on error
    repo.remotes["origin"].pull()

    # read the "database"
    # - JSON file should be enough
    # - entries:
        # - SN
        # - TID
        # - creator
        # - usage/comment
        # - timestamp
        
        # maybe
            # - internal usage vs for partner certificate creation
    
    # create a new set of SN + TID
    
    # add them to the "database"
    # - creator
    # - comment
    # exit on error
    
    # nice to have - edit README.md
    # README could have a more human readable table for the existing SN + TIDS
    
    # commit and push changes
    # exit on error
    repo.index.add("main.py")
    repo.index.commit("main") # should be generated dynamically
    repo.remotes["origin"].push()
    
    # print out the SN +TID

if __name__ == "__main__":
    main()