.ONESHELL:
error:
	@echo "You haven't selected a language for the document!"
	@echo "Usage: make RO/EN/FR/DE"

RO: selectRO
	@rm -f *.log *.aux

selectRO: facRO
	@read -p "Alege facultatea: " faculty;
	@read -p "Tip (Proiect/Lucrare de laborator/...): " docType;
	@read -p "Disciplină: " subject;
	@read -p "Titlu: " title;
	@read -p "Prenume: " firstName;
	@read -p "Nume: " lastName;
	@read -p "Grupă: " group;
	pdflatex -interaction=scrollmode --jobname="Pagină de titlu" "\newcommand{\docType}{$$docType} \newcommand{\subject}{$$subject} \renewcommand{\title}{$$title} \newcommand{\firstName}{$$firstName} \newcommand{\lastName}{$$lastName} \newcommand{\group}{$$group} \input{./faculties/RO/$$faculty.tex}"

facRO:
	$(info Opțiuni:
	FAIMA - Facultatea de Antreprenoriat, Ingineria și Managementul Afacerilor
	FAC - Facultatea de Automatică și Calculatoare
	FCASM - Facultatea de Chimie Aplicată și Știința Materialelor
	FETTI - Facultatea de Electronică, Telecomunicații și Tehnologia Informației
	FE - Facultatea de Energetică
	FISB - Facultatea de Ingineria Sistemelor Biotehnice
	FIA - Facultatea de Inginerie Aerospațială
	FIE - Facultatea de Inginerie Electrică
	FIIR - Facultatea de Inginerie Industrială și Robotică
	FILS - Facultatea de Inginerie în Limbi Străine
	FIMM - Facultatea de Inginerie Mecanică și Mecatronică
	FIM - Facultatea de Inginerie Medicală
	FSIM - Facultatea de Știința și Ingineria Materialelor
	FSA - Facultatea de Științe Aplicate
	FT - Facultatea de Transporturi)

EN: selectEN
	@rm -f *.log *.aux

selectEN: facEN
	@read -p "Choose the faculty: " faculty;
	@read -p "Type (Project/Lab work/...): " docType;
	@read -p "Subject: " subject;
	@read -p "Title: " title;
	@read -p "First name: " firstName;
	@read -p "Last name: " lastName;
	@read -p "Group: " group;
	pdflatex -interaction=scrollmode --jobname="Title page" "\newcommand{\docType}{$$docType} \newcommand{\subject}{$$subject} \renewcommand{\title}{$$title} \newcommand{\firstName}{$$firstName} \newcommand{\lastName}{$$lastName} \newcommand{\group}{$$group} \input{./faculties/EN/$$faculty.tex}"

facEN:
	$(info Options:
	FAIMA - Faculty of Entrepreuneurship, Business Engineering and Management
	FAC - Faculty of Automatic Control and Computers
	FCASM - Faculty of Applied Chemistry and Materials Science
	FETTI - Faculty of Electronics, Telecommunications and Information Technology
	FE - Faculty of Power Engineering
	FISB - Faculty of Biotechnical Systems Engineering
	FIA - Faculty of Aerospace Engineering
	FIE - Faculty of Electrical Engineering
	FIIR - Faculty of Industrial Engineering and Robotics
	FILS - Faculty of Engineering in Foreign Languages
	FIMM - Faculty of Mechanical Engineering and Mechatronics
	FIM - Faculty of Medical Engineering
	FSIM - Faculty of Material Science and Engineering
	FSA - Faculty of Applied Sciences
	FT - Faculty of Transports)

FR: selectFR
	@rm -f *.log *.aux

selectFR:
	@read -p "Catégorie (Projet/Travail de labo/...): " docType;
	@read -p "Matière: " subject;
	@read -p "Titre: " title;
	@read -p "Prénom: " firstName;
	@read -p "Nom de famille: " lastName;
	@read -p "Groupe: " group;
	pdflatex -interaction=scrollmode --jobname="Page de titre" "\newcommand{\docType}{$$docType} \newcommand{\subject}{$$subject} \renewcommand{\title}{$$title} \newcommand{\firstName}{$$firstName} \newcommand{\lastName}{$$lastName} \newcommand{\group}{$$group} \input{./faculties/FILS/FR/FILS.tex}"

DE: selectDE
	@rm -f *.log *.aux

selectDE:
	@read -p "Art (Projekt/Laborarbeit/...): " docType;
	@read -p "Fach: " subject;
	@read -p "Titel: " title;
	@read -p "Vorname: " firstName;
	@read -p "Familienname: " lastName;
	@read -p "Gruppe: " group;
	pdflatex -interaction=scrollmode --jobname="Titelseite" "\newcommand{\docType}{$$docType} \newcommand{\subject}{$$subject} \renewcommand{\title}{$$title} \newcommand{\firstName}{$$firstName} \newcommand{\lastName}{$$lastName} \newcommand{\group}{$$group} \input{./faculties/FILS/DE/FILS.tex}"

clear:
	@rm -f *.pdf
