import { useState } from "react";
import { LetterProps } from "@interfaces";

function getRandomColor(): string {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
}

export default function Letter(props: LetterProps) {
  const [color] = useState(getRandomColor());

  return (
    <span
      className={`font-itim select-none ${
        props.profile ? "text-profile" : "text-contact"
      }`}
      style={{ color }}
    >
      {props.name.charAt(0).toUpperCase()}
    </span>
  );
}
