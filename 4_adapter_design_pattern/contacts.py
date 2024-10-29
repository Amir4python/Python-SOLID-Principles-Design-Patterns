import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

#contact data class
class Contact:
    def __init__(self, name, email, phone, isFriend):
        self.name = name
        self.email = email
        self.phone = phone
        self.isFriend = isFriend

    def __str__(self):
        return f"{self.name} {self.email} {self.phone} {'(Friend)' if self.isFriend else ''}"

#base class for reading file data
class FileReader(ABC):
    def __init__(self, fileName):
        self.fileName = fileName

    @abstractmethod
    def read(self):
        pass


class JSONReader(FileReader):


    def read(self):
        with open(self.fileName, 'r') as f:
            return json.load(f)


class XMLReader(FileReader):

    def read(self):
        with open(self.fileName, 'r') as f:
            return f.read()

#abstract base class for all Contact Adapters
class ContactAdapter(ABC):
    def __init__(self, data: FileReader):
        self.data = data

    @abstractmethod
    def get_contacts(self):  #list of Contact objects
        pass


class JSONContactAdapter(ContactAdapter):
    def get_contacts(self):
        contacts = []

        contactsDict=self.data.read()
        for contact in contactsDict['contacts']:
            contacts.append(Contact(contact['full_name'], contact['email'], contact['phone_no'], contact['isFriend']))
        return contacts

#specific implementation of adapter for XML
class XMLContactAdapter(ContactAdapter):
    def get_contacts(self):
        contacts = []
        root = ET.fromstring(self.data.read())
        for elem in root.iter():
            if elem.tag == 'contact':
                name = elem.find('full_name').text
                email = elem.find('email').text
                phone = elem.find('phone_no').text
                isFriend = elem.find('is_friend').text.lower() == 'true'
                contacts.append(Contact(name, email, phone, isFriend))
        return contacts


def print_contact_data(contacts: ContactAdapter):
    for contact in contacts.get_contacts():
        print(contact)  #got str of each contact object


if __name__ == '__main__':
    json_reader = JSONReader('contacts.json')
    xml_reader = XMLReader('contacts.xml')

    json_adapter = JSONContactAdapter(json_reader)
    xml_adapter = XMLContactAdapter(xml_reader)

    print_contact_data(json_adapter)
    print_contact_data(xml_adapter)
