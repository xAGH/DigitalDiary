import { CSSProperties } from "react";

export default interface InputProps {
  name: string;
  id: string;
  value?: string;
  placheholder?: string;
  required?: boolean;
  disabled?: boolean;
  customStyles?: string;
  onChangeHandler?: any;

}