import { useState } from "react";
import { ProfileProps } from "@interfaces";
import Letter from "../components/Letter";
import ProfileOptions from "../components/ProfileOptions";
import { motion } from "framer-motion";
import useIsFirstRender from "../hooks/useFirstRender";

export default function Profile(user: ProfileProps) {
  const [showOptions, setShowOptions] = useState(false);
  const small = { opacity: 0, scale: 0.5 };
  const normal = { opacity: 1, scale: 1 };
  const isFirst = useIsFirstRender();

  return (
    <div className="flex relative">
      <motion.div
        whileHover={{ scale: 1.04 }}
        className="bg-white flex flex-col items-center rounded-full w-44 h-44 cursor-pointer"
        onClick={() => {
          setShowOptions(!showOptions);
        }}
      >
        <Letter name={user.name} profile={true} />
      </motion.div>
      {!isFirst && (
        <motion.div
          initial={showOptions ? small : normal}
          animate={showOptions ? normal : small}
          transition={{ duration: 0.5 }}
          className={`flex items-center absolute gap-10 left-48 w-72 top-1/4 ${
            !showOptions ? "pointer-events-none" : ""
          }`}
        >
          <ProfileOptions />
        </motion.div>
      )}
      ;
    </div>
  );
}
