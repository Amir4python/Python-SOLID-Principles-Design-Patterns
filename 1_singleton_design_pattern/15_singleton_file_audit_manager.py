"""
EXERCISE:
    1. Create a Singleton Implementation which will log all the messages to a common file
    a. Imagine you wanted to audit all the actions in your application.
    b. It would make sense to log that into a file with guarantee that all
    callers will write to the same file. make the file configurable.
        For each call to FileAuditManager your code will generate a timestamp
        and write the message entry into the file with newline character at the end of each message.
    2. make your implementation thread safe.
"""


import threading
import datetime

class FileAuditManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(FileAuditManager, cls).__new__(cls)
            return cls._instance


    def log(self, message):
        with self._lock:
            with open('audit.log', 'a') as audit_log:
                audit_log.write(f'{datetime.datetime.now()} {message}\n')

def test_file_audit_manager():
    manager=FileAuditManager()
    manager.log('Test message')

if __name__ == '__main__':
    # manager1 = FileAuditManager()
    # manager2 = FileAuditManager()
    #
    # print(manager1 is manager2)
    # manager1.log('Welcome to python lessons')
    # manager1.log('Learn about desing patterns in python')
    # manager2.log('Welcome to singleton pattern')
    # manager2.log('Welcome to singleton pattern with thread safe implementation')
    # manager1.log('learn about meta class and threading in python')
    # manager2.log('Welcome to singleton pattern with thread safe implementation')

    threads=[]
    for i in range(5):
        thread=threading.Thread(target=test_file_audit_manager)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()