'''Allow customization of the process title.'''

def setproctitle(title: str) -> None: 
    '''Set title as the title for the current process.'''
    ...

def getproctitle() -> str: 
    '''Get the current process title.'''
    ...

def setthreadtitle(title: str) -> None: 
    '''Set title as the title for the current thread.'''
    ...

def getthreadtitle() -> str: 
    '''Get the current thread title.'''
    ...

