import Search from "../components/Search";
import { useState } from "react";
import Contact from "../components/Contact";
import { ContactsProps, ContactProps } from "@interfaces";

export default function Contacts(props: ContactsProps) {
  const [filter, setFilter] = useState("");

  let contacts = props.contacts;

  const filterIn = (toFilter: string) =>
    toFilter.toLocaleLowerCase().indexOf(filter.toLocaleLowerCase()) !== -1;

  return (
    <div className="space-y-10 py-8 p-10 bg-white rounded-2xl flex-col flex">
      <Search filterText={filter} onChangeHanlder={setFilter} />

      {contacts.length > 0 ? (
        <div className="overflow-y-scroll space-y-4">
          {contacts
            .filter(
              (contact: ContactProps) =>
                filterIn(contact.name) || filterIn(contact.phone)
            )
            .map((contact, index) => (
              <Contact key={index} {...contact} />
            ))}
        </div>
      ) : (
        <p className="text-3xl">No tienes contactos agregados</p>
      )}
    </div>
  );
}
