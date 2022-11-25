import Icon from "./Icon";

export default function ProfileOptions() {
  let btnClass: string = "flex items-baseline justify-between gap-6";

  return (
    <div
      className={
        "text-3xl bg-white  rounded-xl select-none flex flex-col px-5 py-2"
      }
    >
      <button className={btnClass} onClick={logout}>
        <Icon icon="person" />
        <span>Editar perfil</span>
      </button>

      <button className={btnClass} onClick={editProfile}>
        <Icon icon="logout" />
        <span>Cerrar sesión</span>
      </button>
    </div>
  );
}

function logout() {
  alert("Logout");
}

function editProfile() {
  alert("Profule edit");
}
