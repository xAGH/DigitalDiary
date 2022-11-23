import { ContactProps } from "@interfaces";
import ContactsPage from "./pages/ContactsPage";

export default function App() {
  let contacts: ContactProps[] = [
    {
      name: "Alejandro Giraldo Herrera ",
      phone: "3013258495",
      id: 1,
    },
    {
      name: "Viki ",
      phone: "3013258495",
      id: 1,
    },
    {
      name: "Michael ",
      phone: "3013328495",
      id: 1,
    },
    {
      name: "Michael ",
      phone: "3013328495",
      id: 1,
    },
    {
      name: "Michael ",
      phone: "3013328495",
      id: 1,
    },
    {
      name: "Michael ",
      phone: "3013328495",
      id: 1,
    },
    {
      name: "Michael ",
      phone: "3013328495",
      id: 1,
    },
  ];
  return (
    <div className="h-screen flex">
      <ContactsPage
        contacts={{ contacts }}
        user={{ name: "Alejo", phone: "301324389" }}
      />
    </div>
  );
}
