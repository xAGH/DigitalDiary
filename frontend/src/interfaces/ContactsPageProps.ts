import ContacsProps from "./ContactsProps"

export default interface ContactsPageProps {
  contacts: ContacsProps, 
  user: {
    name: string, 
    phone: string
  }
}