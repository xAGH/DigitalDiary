import Letter from "./Letter";
import Options from "./Options";
import { ContactProps } from "@interfaces/";

export default function Contact(contact: ContactProps) {
  let infoClass =
    "inline-block text-3xl overflow-hidden whitespace-nowrap text-ellipsis";

  return (
    <div className="bg-primary rounded-xl py-2 flex justify-evenly">
      <Letter name={contact.name} />

      <div className="flex flex-col justify-around w-1/2">
        <span className={infoClass}>{contact.name}</span>
        <span className={infoClass}>{contact.phone}</span>
      </div>

      <div>
        <Options id={contact.id} />
      </div>
    </div>
  );
}
