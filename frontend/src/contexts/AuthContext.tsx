import { createContext, Dispatch, SetStateAction, useState } from "react";
import { AuthContextProps } from "@interfaces";

interface AuthContextData {
  auth: boolean;
  setAuth: Dispatch<SetStateAction<boolean>>;
}

const AuthContext = createContext({} as AuthContextData);

export function AuthProvider(props: AuthContextProps) {
  const [authenticated, setAuthenticated] = useState(false);

  const manageAuth = () => {
    authenticated ? setAuthenticated(false) : setAuthenticated(true);
  };

  const data: AuthContextData = {
    auth: authenticated,
    setAuth: manageAuth,
  };

  return (
    <AuthContext.Provider value={data}>{props.children}</AuthContext.Provider>
  );
}
