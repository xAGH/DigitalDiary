import { InputProps } from "@interfaces/";

export default function Input(props: InputProps) {
  return (
    <input
      type="text"
      id={props.id}
      value={props.value}
      className={`border-none outline-none rounded-xl w-full px-5 py-2 bg-primary text-2xl ${props.customStyles}`}
      placeholder={props.placheholder}
      required={props.required}
      disabled={props.disabled}
      onChange={
        props.onChangeHandler
          ? (e) => {
              props.onChangeHandler(e.target.value);
            }
          : () => {}
      }
    />
  );
}
