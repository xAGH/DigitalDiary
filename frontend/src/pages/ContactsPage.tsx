import Contacts from "../containers/Contacts";
import ContactForm from "../containers/ContactForm";
import ContactsPageProps from "@interfaces/ContactsPageProps";
import Profile from "../containers/Profile";

export default function ContactsPage(props: ContactsPageProps) {
  return (
    <div className="w-10/12 h-85vh m-auto bg-primary flex  rounded-2xl justify-evenly p-10">
      <Contacts {...props.contacts} />
      <div className="flex flex-col items-center justify-evenly">
        <Profile name={props.user.name} phone={props.user.phone} />
        <ContactForm />
      </div>
    </div>
  );
}
