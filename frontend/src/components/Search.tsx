import Icon from "./Icon";
import { InputProps, SearchProps } from "@interfaces";
import Input from "./Input";

export default function Search(props: SearchProps) {
  const searchInputOptions: InputProps = {
    id: "search",
    name: "search",
    placheholder: "Buscar contacto...",
    value: props.filterText,
    onChangeHandler: props.onChangeHanlder,
    customStyles: "rounded-l-none text-xl",
  };

  return (
    <form>
      <div className="flex">
        <label htmlFor="search">
          <Icon
            icon="search"
            customClasses="text-3xl p-[0.4rem] pl-5 bg-primary rounded-l-xl text-gray-600"
          />
        </label>
        <Input {...searchInputOptions} />
      </div>
    </form>
  );
}
