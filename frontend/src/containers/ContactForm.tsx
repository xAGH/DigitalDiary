import Input from "../components/Input";
import { ContactFormProps } from "@interfaces";
import Icon from "../components/Icon";

export default function ContactForm(props: ContactFormProps) {
  const inputStyles = "bg-white w-[80%]";

  return (
    <div className="w-[50rem] flex flex-col gap-10 items-center">
      <p className="text-5xl">
        {props.action ? props.action : "Crear nuevo contacto"}
      </p>

      <Input
        id="name"
        name="name"
        placheholder="Nombre del contacto"
        customStyles={inputStyles}
      />
      <Input
        id="phone"
        name="phone"
        placheholder="Teléfono del contacto"
        customStyles={inputStyles}
      />

      <button onClick={() => {}}>
        <Icon icon="add" customClasses="text-7xl text-green-500 mt-5" />
      </button>
    </div>
  );
}
