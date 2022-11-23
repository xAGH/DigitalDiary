import { OptinsProps } from "@interfaces";
import Icon from "./Icon";

export default function Options(props: OptinsProps) {
  let circle: string = "rounded-full p-2 flex items-center justify-center";

  const handleEditClick = () => {};
  const handleDeleteClick = () => {};

  return (
    <div className="flex flex-col gap-2 justify-around h-full w-fit">
      <button className={`${circle} bg-edit`} onClick={handleEditClick}>
        <Icon icon="edit" />
      </button>

      <button className={`${circle} bg-delete`} onClick={handleDeleteClick}>
        <Icon icon="close" />
      </button>
    </div>
  );
}
