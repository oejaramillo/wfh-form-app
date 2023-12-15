const jobAds = [
    "Busco jóvenes de educacion superior para trabajo flexible con estudios. Se efectúa selección de personal por medio del envio de curriculum a partime@hotmail.cl. Posteriormente se cita a entrevista en la empresa con supervisor de area.\r\n\r\nPor tres horas semanales trabajadas en la empresa, el sueldo mensual es de $70.000. La idea es que tengas disponibilidad y ganas de aprender y trabajar, el horario es el siguiente:\r\n\r\n- Lunes (de 18:00 a 19:00)\r\n\r\n- Miercoles (de 18:00 a 19:00)\r\n\r\n- Viernes (de 11:00 a 12:00)\r\n\r\n\r\n\r\nHorario Flexible segun carga académica.\r\n\r\nLa empresa busca gente con aspiraciones reales, para proporcionar nuevos ascensos.\r\n\r\nCapacitaciones Gratuitas en areas de personalidad, autoconfianza, modelacion de proyectos, liderzgo entre otros, para el desempeño de roles.\r\n\r\nNo requiere experiencia previa ni estudios relacionados a ningun area en particular, te enseñaremos lo que necesitas.\r\n\r\nSi te gusta la idea, solicita una entrevista envíando tu curriculum a partime@hotmail.cl y contacta con Raul Barria Murua, Monitor de equipo",
    "\r\nImportante empresa Multinacional,  lider en su industria requiere las mejores personas para desempeñarse en distintas actividades las cuales puede desarrollar y realizar desde su casa, oficina o de nuestras oficinas.\r\n\r\n- Supervisión\r\n- Distribucion\r\n- Servicio al cliente\r\n- Ventas\r\n- Telemarketing, entre otras\r\n\r\nCapacitacion inmediata, no se requiere experiencia previa y debe tener mínimo 18 años sin limite de edad, ser  proactivo(a) y tener ganas de trabajar en equipo.\r\nInteresados enviar CV esta semana a trabajeonline@yahoo.es\r\nCupos limitados\r\n",
    "Komatsu Cummins Chile Arrienda S.A., empresa líder en venta de arriendos de maquinaria y equipos usados, requiere contratar, para su casa matriz ubicada en Lampa a un:\r\n  \r\nJefe de Ventas Terreno\r\n  \r\nNuestra búsqueda se orienta a profesionales que cuenten con al menos 5 años de experiencia en venta de maquinaria y/o equipos de movimiento de tierra, con experiencia de trabajo en terreno y disponibilidad para realizarlo, y que hayan liderado equipos de ventas. Debe poseer dominio de herramientas Office, licencia de conducir clase B vigente y disponibilidad para trabajar en Lampa.\r\n  \r\nBuscamos personas con alta orientación al cumplimiento de metas, manejo de equipos de trabajo, orientación al cliente y disponibilidad para desempeñarse en terreno, supervisando al equipo y apoyando en las ventas de arriendo de equipos.",
    "Responsable del desarrollo del área de ventas de los productos de la clínica en los canales: isapres, seguros y empresas.\r\n\r\nSiendo algunas actividades a desarrollar:\r\n• Gestión de ventas de grandes cuentas: isapres\r\n• Supervisión de canales de venta por línea (seguros, servicios clínicos, empresas)\r\n• Promover la innovación y perfeccionamiento continuo en el portafolio de servicios\r\n• Velar porque la estructura de precios considerará la estructura de costos, posicionamiento y un margen que nos permita cumplir con la visión y misión \r\n• Realizar seguimiento de objetivos comerciales\r\n• Diseñar e implementar un modelo de atención personalizado.\r\n• Monitoreo permanente de la competencia\r\n\r\nConocimientos específicos: del mercado de salud \r\n\r\nExperiencia: profesional con al menos 6 años de experiencia, al menos 4 años en el área de salud (isapre o prestador de salud). \r\nQue haya tenido personas a cargo o haya liderado proyectos.\r\n\r\nHabilidades/destrezas: \r\n• Para establecer relaciones interpersonales\r\n• Proactividad\r\n• Flexibilidad y tolerancia a la frustración\r\n• Capacidad de negociación y liderazgo\r\n• Capacidad para trabajar bajo presión\r\n• Con fuerte orientación al logro \r\n• Buena capacidad de planificación y organización"
];

const jobAdContainer = document.getElementById("jobAdContainer");
const jobAdForm = document.getElementById("jobAdForm");

let currentIndex = 0;

// Function to display the next job ad
function displayNextJobAd() {
    if (currentIndex < jobAds.length) {
        jobAdContainer.innerHTML = jobAds[currentIndex];
        currentIndex++;
    } else {
        jobAdContainer.innerHTML = "Gracias por ayudarnos";
        jobAdForm.style.display = "none";
    }
}

// Event listener for form submission
jobAdForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const classification = document.querySelector('input[name="classification"]:checked');
    if (!classification) {
        alert("Por favor selecciones una opción.");
        return;
    }

    const formData = {
        jobAd: jobAdContainer.innerHTML,
        classification: classification.value,
    };

    console.log(JSON.stringify(formData));

    // Display the next job ad
    displayNextJobAd();
});

// Initial display
displayNextJobAd();
