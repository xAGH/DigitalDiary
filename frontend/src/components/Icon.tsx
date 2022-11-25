import { IconProps } from "@interfaces";

export default function Icon(props: IconProps) {
  return (
    <span className={`material-symbols-outlined ${props.customClasses}`}>
      {props.icon}
    </span>
  );
}
