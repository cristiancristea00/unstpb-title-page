.ONESHELL:
build: options title clean

options:
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

title:
	@read -p "Alege facultatea: " faculty;
	@read -p "Tip: " docType;
	@read -p "Disciplină: " subject;
	@read -p "Titlu: " title;
	@read -p "Prenume: " firstName;
	@read -p "Nume: " lastName;
	@read -p "Grupă: " group;
	pdflatex -interaction=scrollmode --jobname="Pagină de titlu" "\newcommand{\docType}{$$docType} \newcommand{\subject}{$$subject} \renewcommand{\title}{$$title} \newcommand{\firstName}{$$firstName} \newcommand{\lastName}{$$lastName} \newcommand{\group}{$$group} \input{./faculties/$$faculty.tex}"

clean:
	rm -f *.log *.aux
