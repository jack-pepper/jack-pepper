
```bash
int main()
{
  Profile my; // 🪪
  
  my._name = "Morgan";
  my._school = 42; /* Nice (France) */
  my._areasOfInterest = {

    "Software_Architecture" : "Designing scalable and efficient systems";
    "Web Development"       : "Javascript";
    "Game Development"      : "Unity, C#";
    "AI & Machine Learning" : "Natural language processing, cognitive science applications";
  
  };
  my._languages = { "English", "Русский", "Français", "汉语", "Esperanto" };
  my._assets = { "ambitious", "pragmatic", "adaptable" };
  my._currentTarget = "study";
  
  Background previousCarrier; // 📚
  
  previousCarrier._field = "Early education";
  previousCarrier._speciality = "Teaching French as a Foreign Language";
  previousCarrier._top[3] = { "Trainer & Coordinator", "Preschool Designer", "School Director" };
  
  Company business; // 💼
  
  business._status = "IE"; /* Individual Entrepreneur */
  business._commercialName = "MARIDO";
  business._services = {
    
    "educational" : "private tutoring";
    "linguistic"  : "translation & localisation (en/ru/eo > fr); copyrighting"
    "informatics" : "undefined";
  
  }
  business._website = "https://www.marido.fr";

  Skills stack; // 🛠️

  stack.os[3] = { "Linux", "MacOS", "Windows" };
  stack.languages.computer = { "C", "C++", "HTML", "Javascript", "Python" };
  stack.ai_tools = { "GPT", "Claude", "Copilot", "Suno" };
  
  if ( wantToKnowMore )
    sendMessage( "marido.entreprise[at]gmail.com" );
  else
    std::cout << "Thanks for reading, have a nice day!" << '\n';

  return ( $? );
}
`
