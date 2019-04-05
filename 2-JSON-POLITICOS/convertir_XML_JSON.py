# test_jsonschema_unix.py
# A program to try the jsonschema Python library.
# Uses it to validate some JSON data.
# Follows the Unix convention of writing normal output to the standard 
# output (stdout), and errors to the standard error output (stderr).
# Author: Vasudev Ram
# Copyright 2015 Vasudev Ram

from __future__ import print_function
import sys
import json
import jsonschema
from jsonschema import validate

# Create the schema, as a nested Python dict, 
# specifying the data elements, their names and their types.
schema = {
     
     "properties": {
            "politico": {
                "title": "Politico",
                "type": "array",
                "items": [
                    {
"type": "object",
                        "properties": {
                            "@id": {
                                "title": "Id",
                                "Minimum": 0,
                                "type": "integer"
                            },
                            "datosPersonales": {
                                "title": "Datos Personales",
                                "type": "object",
                                "properties": {
                                    "img": {
                                        "title": "Imagen",
                                        "description": "Fotografía del politico",
                                        "type": "object",
                                        "properties": {
                                            "@url": {
                                                "title": "Url",
                                                "type": "string",
                                                "format": "uri"
                                            }
                                        },
                                        "required": [
                                            "@url"
                                        ]
                                    },
                                    "nombres": {
                                        "title": "Nombre",
                                        "type": "string"
                                    },
                                    "apellidoPaterno": {
                                        "title": "Apellido Paterno",
                                        "type": "string"
                                    },
                                    "apellidoMaterno": {
                                        "title": "Apellido Materno",
                                        "type": "string"
                                    },
                                    "estadoCivil": {
                                        "title": "Estado Civil",
                                        "enum": [
                                            "Soltero",
                                            "Casado",
                                            "Viudo",
                                            "Divorciado",
                                            "Separado",
                                            "Conviviente"
                                        ],
                                        "type": "string"
                                    },
                                    "profesion": {
                                        "title": "Profesión",
                                        "type": "string"
                                    },
                                    "nacionalidad": {
                                        "title": "Nacionalidad",
                                        "type": "string"
                                    },
                                    "fechaNacimiento": {
                                        "title": "Fecha Nacimiento",
                                        "format": "date",
                                        "type": "string"
                                    },
                                    "lugarNacimiento": {
                                        "title": "Lugar Nacimiento",
                                        "type": "string"
                                    },
                                    "fechaDefuncion": {
                                        "title": "Fecha Defunción",
                                        "format": "date",
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "lugarDefuncion": {
                                        "title": "Lugar Defunción",
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                },
                                "required": [
                                    "img",
                                    "nombres",
                                    "apellidoPaterno",
                                    "apellidoMaterno",
                                    "estadoCivil",
                                    "profesion",
                                    "nacionalidad",
                                    "fechaNacimiento",
                                    "lugarNacimiento",
                                    "fechaDefuncion",
                                    "lugarDefuncion"
                                ]
                            },
                              "trayectorias": {
                                "title": "Trayectorias Politicas",
                                "type": "object",
                                "properties": {
                                    "trayectoria": {
                                        "title": "Trayectoria",
                                        "type": "object",
                                        "properties": {
                                            "tipoParlamentario": {
                                                "title": "Tipo Parlamentario",
                                            
                                               "enum": [
                                                    "Senador",
                                                    "Diputado"
                                                ],
                                                "type": "string"
                                            },
                                            "partidoPolitico": {
                                                "title": "Partido Politico",
                                                 "enum": [
                                                "Unión Demócrata Independiente",
                                                    "Renovación Nacional",
                                                    "Partido Demócrata Cristiano",
                                                    "Partido Por la Democracia",
                                                    "Partido Comunista de Chile",
                                                    "Partido Socialista de Chile",
                                                    "Evolución Política",
                                                    "Revolución Democrática",
                                                    "País Progresista",
                                                    "Partido Radical de Chile",
                                                    "Federación Regionalista Verde Social",
                                                    "Partido Humanista",
                                                    "Partido Liberal de Chile",
                                                    "Poder Ciudadano",
                                                    "Partido Igualdad",
                                                    "Partido Ecologista Verde",
                                                    "Partido Regionalista Independiente Demócrata",
                                                    "Ciudadanos",
                                                    "Izquierda Anticapitalista de los Trabajadores",
                                                    "Nuevo Tiempo",
                                                    "Partido Anticorrupción Chile",
                                                    "Movimiento por la Tierra, el Trabajo y la Libertad",
                                                    "Partido Orden Republicano Por Mi Patria",
                                                    "Partido Político Chile Feminista",
                                                    "Unidad Cristiana Nacional"
                                            
                                                ],
                                                "type": "string"
                                              
                                            },
                                            "periodoInicio": {
                                                "title": "Periodo Inicio",
                                                "Minimum": 1810,
                                                "type": "integer"
                                            },
                                            "periodoTermino": {
                                                "title": "Periodo Término",
                                                "Minimum": 1810,
                                                "type": "integer"
                                            },
                                            "divisionElectoral": {
                                                "title": "División Electoral",
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "tipoParlamentario",
                                            "partidoPolitico",
                                            "periodoInicio",
                                            "periodoTermino",
                                            "divisionElectoral"
                                        ]
                                    }
                                },
                                "required": [
                                    "trayectoria"
                                ]
                            }, "reseniaResumen": {
                                "title": "Reseña Resumen",
                                "description": "Resumen reseña bibliografica",
                                "type": "string"
                            },
                            "familiaJuventud": {
                                "title": "Familia Juventud",
                                "description": "reseña epoca de juventud y familiar",
                                "type": "string"
                            },
                            "estudiosVidaLaboral": {
                                "title": "Estudios y Vida Laboral",
                                "description": "reseña epoca de estudio y vida laboral",
                                "type": "string"
                            },
                            "trayectoriaPoliticaPublica": {
                                "title": "Trayectoria Politica y Publica",
                                "description": "reseña trayectoria politica y publica",
                                "type": "string"
                            },
                            "hemiciclos": {
                                "type": "object",
                                "properties": {
                                    "hemiciclo": {
                                        "type": "object",
                                        "properties": {
                                            "periodoInicio": {
                                                "title": "Periodo Inicio",
                                                "Minimum": 1810,
                                                "type": "integer"
                                            },
                                            "periodoTermino": {
                                                "title": "Periodo Término",
                                                "Minimum": 1810,
                                                "type": "integer"
                                            },
                                            "descripcion": {
                                                "title": "Descripción",
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "periodoInicio",
                                            "periodoTermino",
                                            "descripcion"
                                        ]
                                    }
                                },
                                "required": [
                                    "hemiciclo"
                                ]
                            },   "bibliografias": {
                                "type": "object",
                                "properties": {
                                    "bibliografia": {
                                        "type": "array",
                                        "items": [
                                            {
                                            "type": "object",
                                                "properties": {
                                                    "@url": {
                                                        "title": "Url",
                                                        "type": "string",
                                                        "format": "uri"
                                                    },
                                                    "nombre": {
                                                        "title": "Nombre",
                                                        "type": "string"
                                                    },
                                                    "editorial": {
                                                        "title": "Editorial",
                                                        "type": "string"
                                                    },
                                                  "ano": {
                                                        "title": "Año",
                                                        "Minimum": 0,
                                                        "type": "integer"
                                                    },
                                                     "descripcion": {
                                                        "title": "Descripción",
                                                        "type": "string"
                                                    },
                                                    "isbn": {
                                                        "title": "isbn",
                                                        "type": "string"
                                                    },
                                                  
                                                  "disponible": {
                                                        "title": "Disponibilidad",
                                                        "Minimum": 0,
                                                        "type": "integer"
                                                    }
                                                },
                                                     "required": [
                                                    "@url",
                                                    "nombre",
                                                    "editorial",
                                                    "ano",
                                                    "descripcion",
                                                    "isbn",
                                                    "disponible"
                                                ]
                                            }
                                        ]
                                    }
                                },
                                "required": [
                                    "bibliografia"
                                ]
                            }
                        },
                         "required": [
                            "@id",
                            "datosPersonales",
                            "trayectorias",
                            "reseniaResumen",
                            "familiaJuventud",
                            "estudiosVidaLaboral",
                            "trayectoriaPoliticaPublica",
                            "hemiciclos",
                            "bibliografias"
                        ]
                    }
                ]
                        }
                         },
        "required": [
            "politico"
        ]
                  
}

print("Testing use of jsonschema for data validation.")
print("Using the following schema:")
print(schema)
print("Pretty-printed schema:")
print(json.dumps(schema, indent=4))

# The data to be validated:
# Two records OK, three records in ERROR.
data = \
[{
     "politico": [
            { 
"@id": 1968,
                "datosPersonales": {
                    "img": {
                        "@url": "http://biografias.bcn.cl/images/9/9a/Mariana_Aylwin_Oyarz%C3%BAn.jpg"
                    },
                    "nombres": "Mariana",
                    "apellidoPaterno": "Aylwin",
                    "apellidoMaterno": "Oyarzún",
                    "estadoCivil": "Casado",
                    "profesion": "Profesor de Estado en Historia, Geografía y Educación Cívica",
                    "nacionalidad": "Chilena",
                    "fechaNacimiento": "1949-07-13",
                    "lugarNacimiento": "Santiago, Chile",
                    "fechaDefuncion": "",
                    "lugarDefuncion": ""
                },
    "trayectorias": {
                    "trayectoria": {
                        "tipoParlamentario": "Diputado",
                        "partidoPolitico": "Partido Demócrata Cristiano",
                        "periodoInicio": 1994,
                        "periodoTermino": 1998,
                        "divisionElectoral": "Distrito N° 26"
                    }
                },
     "reseniaResumen": "Mariana Aylwin Oyarzún (Santiago, 13 de julio de 1949). Profesora y política del Partido Demócrata Cristiano. Diputada por el Distrito N° 26, comuna La Florida, Región Metropolitana, para el período legislativo 1994-1998. Ministra de Educación durante el Gobierno de Ricardo Lagos Escobar entre 2000 y 2003. Consejera Regional de la Región Metropolitana, entre marzo de 2014 y noviembre de 2016.",
                "familiaJuventud": "Nació en Santiago, el 13 de julio de 1949. Hija del ex presidente de la República, Patricio Aylwin Azócar y de Leonor Oyarzún Ivanovic.\n            Sobrina del ex diputado Andrés Aylwin Azócar.\n            Casada con Carlos Bascuñán Edwards y tiene cuatro hijos.",
                "estudiosVidaLaboral": "Realizó su etapa escolar en el Colegio Santa Úrsula, en Santiago. Luego ingresó a la Universidad Católica de Chile, donde cursó la carrera de Pedagogía en Historia, Geografía y Educación Cívica, titulandose en el año 1976. Durante su época universitaria y una vez egresada, desarrolló importantes investigaciones relacionadas con su especialidad.\n            En el aspecto laboral, trabajó como profesora de enseñanza media en el Saint George´s College, entre 1974 y 1975. En el año 1979 fue becada por el Instituto Iberoamericano de Cooperación en Madrid, donde realizó una investigación sobre \"La experiencia española de transición a la democracia\". A su regreso, retomó sus clases de profesora de enseñanza media en el Saint George´s, entre los años 1981 a 1986.\n            Consultora para universidad Uniacc y miembro de su Directorio Ejecutivo hasta junio de 2010.\n            Directora Ejecutiva de Corporación Educacional Aprender.\n            Formó parte del directorio de la Fundación Belén Educa y de la Fundación Oportunidad.",
                "trayectoriaPoliticaPublica": "Inició su trayectoria política en 1987, año en que se creó la Concertación de Mujeres por la Democracia. Paralelamente, fue nombrada subdirectora nacional del Departamento de la Mujer del Partido Demócrata Cristiano y secretaria ejecutiva de la Fundación para el Desarrollo y la Cultura Popular.\n            Con el retorno a la democracia, en 1990 se desempeñó como asesora externa de la Dirección de Estudios del Ministerio Secretaría General de la Presidencia, ejerciendo hasta 1994.\n            Durante 1991 fue delegada a la Junta Nacional del Partido Demócrata Cristiano. En 1992 y 1993 integró la directiva central del partido, ocupando la cuarta vicepresidencia nacional. También fue Presidenta del Consejo Político-Técnico y Coordinadora de la Comisión \"Programa de la Concertación de Partidos por la Democracia\".\n            En diciembre de 1993 participó en las elecciones parlamentarias como candidata a diputada por el Distrito Nº26, de correspondía en aquel entonces a la comuna de La Florida, en la Región Metropolitana. Fue electa al obtener 48.309 votos, es decir 32,91% de las preferencias.\n            Para las elecciones parlamentarias de 1997 fue a la reelección por el mismo distrito, pero obtuvo el 20,72% de los sufragios, y no resultó electa.\n            Entre 1999 y 2000, se desempeñó como Coordinadora Nacional del Programa de Mejoramiento de la Calidad y Equidad de la Educación Media (MECE-MEDIA) del Ministerio de Educación.\n            Entre 2000 y 2003 fue Ministra de Educación durante el gobierno de Ricardo Lagos Escobar.\n            En 2006 le correspondió organizar el Congreso Programático de la Democracia Cristiana de octubre de 2007 donde se conmemoraron los 70 años de la fundación de la Falange Nacional.\n            Entre mayo y julio de 2010 participó en el Panel de Expertos para una Educación de Calidad, convocado por el presidente Sebastián Piñera, que trabajó para elaborar propuestas para mejorar el sistema de educación chileno.\n            Entre 2013 y 2015 fuerza pública.\n            En las elecciones para el gobierno regional efectuadas en diciembre de 2013, resultó electa Consejera Regional de la Región Metropolitana de Santiago por la IV circunscripción, al obtener 47.164 votos, es decir el 10,76% de las preferencias. Se desempeñó en este cargo hasta noviembre de 2016 cuando presentó su renuncia con la intención de participar en las elecciones parlamentarias de diciembre de 2017.\n            El 5 de enero de 2018, oficializó su renuncia al Partido Demócrata Cristiano.\n            Entre junio y noviembre de 2018 presidió la comisión presidencial de expertos llamada  Todos al Aula  y que tuvo por objetivo elaborar un plan para desburocratizar la carga administrativa de los colegios del país.\n            En julio de 2018 fue designada para integrar el directorio de la Fundación Chile.",
                "hemiciclos": {
                    "hemiciclo": {
                        "periodoInicio": 1994,
                        "periodoTermino": 1998,
                        "descripcion": "En diciembre de 1993 se presentó como candidata a diputada por el Distrito Nº26, que representaba a la comuna de La Florida, en la Región Metropolitana, para el período 1994 a 1998 y resultó electa.\n                    Integró la Comisión Permanente de Educación, Cultura, Deportes y Recreación, la Comisión de Familia y la Comisión de Salud.\n                    Asistió en representación oficial de la Cámara de Diputados a la III Reunión de Comisión de la Mujer del Parlamento Latinoamericano y Caribeño (PARLATINO) realizada en Buenos Aires, Argentina, en septiembre de 1994."
                    }
                },
         "bibliografias": {
                    "bibliografia": [
                        {
                            "@url": "https://www.bcn.cl/catalogo/detalle_libro?bib=179757&n=1",
                            "nombre": "La reforma al sistema escolar : aportes para el debate",
                            "editorial": "Universidad Diego Portales",
                            "ano": 2007,
                            "descripcion": "252 páginas",
                            "isbn": "9563140071",
                            "disponible": 3
                        },
                        {
                            "@url": "https://www.bcn.cl/catalogo/detalle_libro?bib=153359&n=1",
                            "nombre": "Ley de matrimonio civil : el apoyo de parlamentarios católicos",
                            "editorial": "",
                            "ano": 2004,
                            "descripcion": "Mensaje.(Santiago - Chile).Vol. 53, no. 528 (mayo 2004), p. 26-29, il.",
                            "isbn": "",
                            "disponible": 0
                        },
                        {
                            "@url": "https://www.bcn.cl/catalogo/detalle_libro?bib=177825&n=1",
                            "nombre": "Presentes y distantes : los desafíos del e-learning en la educación superior",
                            "editorial": "Universidad Uniac",
                            "ano": 2006,
                            "descripcion": "92 p. : diagrs.",
                            "isbn": "9563070127",
                            "disponible": 1
                        }
                    ]
                }
},
          {
                "@id": "3145",
                "datosPersonales": {
                    "img": {
                        "@url": "http://biografias.bcn.cl/images/3/30/Mar%C3%ADa_Antonieta_Saa_D%C3%ADaz.jpg"
                    },
                    "nombres": "María Antonieta",
                    "apellidoPaterno": "Saa",
                    "apellidoMaterno": "Díaz",
                    "estadoCivil": "Soltero",
                    "profesion": "Profesora de Castellano",
                    "nacionalidad": "Chilena",
                    "fechaNacimiento": "1943-01-08",
                    "lugarNacimiento": "Santiago, Chile",
                    "fechaDefuncion": "",
                    "lugarDefuncion": ""
                },
                "trayectorias": {
                    "trayectoria": [
                        {
                            "tipoParlamentario": "Diputado",
                            "partidoPolitico": "Partido Por la Democracia",
                            "periodoInicio": 2010,
                            "periodoTermino": 2014,
                            "divisionElectoral": "Distrito N° 17"
                        },
                        {
                            "tipoParlamentario": "Diputado",
                            "partidoPolitico": "Partido Por la Democracia",
                            "periodoInicio": 2006,
                            "periodoTermino": 2010,
                            "divisionElectoral": "Distrito N° 17"
                        },
                        {
                            "tipoParlamentario": "Diputado",
                            "partidoPolitico": "Partido Por la Democracia",
                            "periodoInicio": 2002,
                            "periodoTermino": 2006,
                            "divisionElectoral": "Distrito N° 17"
                        }
                    ]
                },
                "reseniaResumen": "María Antonieta Saa (Santiago, 8 de enero de 1943). Profesora de Estado, mención Castellano, y política del Partido Por la Democracia. Diputada por el Distrito Nº 17, Región Metropolitana, desde 1994 a 2014, por cinco periodos consecutivos. Alcaldesa de la Municipalidad de Conchalí entre 1990 y 1992. Entre 1997 y 1998 fue primera vicepresidenta de la Cámara de Diputados. Consejera Regional por la Circunscripción Provincial Santiago I, períodos 2014-2018 y 2018-2022.",
                "familiaJuventud": "Nació el 8 de enero de 1943, en Santiago. Hija de Raúl Saa y María Antonieta Díaz. Soltera.",
                "estudiosVidaLaboral": "Realizó sus estudios primarios en el Liceo Chileno en Santiago, en el Colegio Beata Imelda de Pitrufquén, y en el Liceo de Niñas de Quillota. Concluyó su educación secundaria en el Liceo N° 7 de Santiago. En 1960, ingresó al Instituto Pedagógico de la Universidad de Chile, donde se tituló de profesora de Castellano, en 1965.\n            Profesionalmente, se desempeñó como profesora del Liceo N° 17 en Santiago. En 1967, se integró a la Corporación de la Reforma Agraria (CORA), como encargada del Programa de Alfabetización Campesina.\n            A partir de 1979, se desempeñó como secretaria de diversos escritores como Jorge Edwards, Matilde Urrutia y Elisa Serrana. Posteriormente, ingresó a trabajar como secretaria al Centro de Formación Técnica Vicente Pérez Rosales en Santiago dónde más tarde, fue jefa de la Carrera de Secretariado.\n            Fue editora social y gremial de la Organización No Gubernamental (ONG) ISIS Internacional, servicio de información y comunicación de las mujeres. En 1982, como parte de la misma institución, viajó a Italia por un año. Al año siguiente, nuevamente en Chile, fue nombrada coordinadora del Círculo de Estudios de la Mujer",
                "trayectoriaPoliticaPublica": "Inició sus actividades públicas como fundadora y primera presidenta del Centro de Alumnas del Liceo N° 7 de Santiago. Posteriormente, fue presidenta de la Juventud Estudiantil Católica de Santiago.\n            En 1969, fue electa presidenta de la Asociación de Trabajadores de la CORA, el que junto a trabajadores del Instituto de Desarrollo Agropecuario (INDAP) y del Servicio Agrícola y Ganadero (SAG), conformaron una agrupación de trabajadores del agro que se integró a la Central Única de Trabajadores (CUT). Como vicepresidenta de esta última agrupación, participó en la CUT.\n            En 1970, se integró al Movimiento de Acción Popular Unitario (MAPU), donde fue miembro de la Directiva Nacional y de la Comisión Política, hasta 1972. Dentro de la misma colectividad, fue parte del grupo fundador del Movimiento de Acción Popular Unitaria-Obrero Campesino (también conocido como MAPU-OC, MOC o MAPU Obrero Campesino). Fue parte de su Comité Central y de la Comisión Política.\n            En 1983, participó en la fundación del Movimiento Feminista. Ese mismo año, ingresó al Partido Socialista (PS). Entre 1985 y 1987, fue miembro del Comité Central y de la Comisión Política de dicha colectividad.\n            En 1986, fue electa dirigenta de la Asamblea de la Civilidad y colaboró en la fundación de la Concertación de Mujeres por la Democracia. Al año siguiente, se integró a la Directiva Central del Partido Por la Democracia (PPD), siendo electa vicepresidenta entre 2003 y 2004.\n            Entre 1990, el presidente Patricio Aylwin la designó alcaldesa de la Municipalidad de Conchalí, cargo en el que estuvo hasta 1992. Durante dicho periodo, impulsó el Consejo Comunal del Niño y Niña, y el Consejo del Adulto Mayor. Asimismo, creó el Centro de Apoyo a la Mujer Víctima de la Violencia Doméstica, el Programa de Apoyo para la Mujer Jefa de Hogar y los Servicios Educativos para Niños.\n            El 13 mayo de 2012 participó en las elecciones internas de su colectividad representando la lista \"Un PPD para el Nuevo Chile\" que obtuvo el segundo lugar con el 36,3% del total de los sufragios. El 11 de junio de 2012 asumió la séptima vicepresidencia en la mesa directiva del Partido Por la Democracia.\n            En 2013 fue electa Consejera Regional (CORE) por la Circunscripción Provincial Santiago I, periodo 2014-2018, correspondiente a las comunas de Renca, Conchalí, Huechuraba, Pudahuel y Quilicura. Una vez asumida en el cargo se integró a las comisiones de Educación, Ordenamiento Territorial e Internacional[1].",
                "hemiciclos": {
                    "hemiciclo": [
                        {
                            "periodoInicio": 2010,
                            "periodoTermino": 2014,
                            "descripcion": "En diciembre de 2009, fue reelecta por quinta vez por el mismo distrito, (periodo legislativo 2010 a 2014). Es integrante de las comisiones permanentes de Familia; de Educación; de Ciencia y Tecnología; y de Superación de Pobreza, Planificación y Desarrollo Social. Junto con la comisión especial del Adulto Mayor. Forma parte del comité parlamentario del Partido Por la Democracia.\n                    Para las elecciones parlamentarias de noviembre de 2013 decidió no presentarse a la reelección por un nuevo periodo."
                        },
                        {
                            "periodoInicio": 2006,
                            "periodoTermino": 2010,
                            "descripcion": "En diciembre de 2005, mantuvo su escaño en la Cámara por el mismo Distrito, (periodo legislativo 2006 a 2010). Integró las comisiones permanentes de Educación, Cultura, Deportes y Recreación; de Familia; de Vivienda y Desarrollo Urbano; y de Constitución, Legislación y Justicia. Junto con las comisiones especiales de Seguridad Ciudadana; y de Drogas. Además de la Comisión Investigadora sobre Platas Públicas entregadas a la Corporación de Desarrollo de Arica y Parinacota (CORDAP).\n                    En misiones al extranjero, participó en la 115ª Asamblea de la Unión Interparlamentaria Mundial, en Suiza y también en su versión número 116, en Indonesia. También integró los grupos interparlamentarios chileno-británico, chileno-holandés y chileno-italiano."
                        },
                        {
                            "periodoInicio": 2002,
                            "periodoTermino": 2006,
                            "descripcion": "En diciembre de 2001, fue reelecta por tercera vez, por su mismo partido e igual Distrito, (período legislativo 2002 a 2006). Mantuvo su trabajo en las mismas comisiones del periodo anterior: Educación, Cultura, Deportes y Recreación; y de Familia."
                        }
                    ]
                },
                "bibliografias": {
                    "bibliografia": {
                        "@url": "https://www.bcn.cl/catalogo/detalle_libro?bib=154300&n=1",
                        "nombre": "La globalización cuestionada",
                        "editorial": "Universidad de Santiago de Chile",
                        "ano": 2004,
                        "descripcion": "186 páginas",
                        "isbn": "9567069921",
                        "disponible": "1"
                    }
                }
            },
            {
                "@id": "2234",
                "datosPersonales": {
                    "img": {
                        "@url": "https://biografias.bcn.cl/images/c/c3/Jos%C3%A9_Luis_Cadem%C3%A1rtori_Invernizzi.jpg"
                    },
                    "nombres": "José Luis",
                    "apellidoPaterno": "Cademártori",
                    "apellidoMaterno": "Invernizzi",
                    "estadoCivil": "Casado",
                    "profesion": "Ingeniero Comercial",
                    "nacionalidad": "Chilena",
                    "fechaNacimiento": "1930-09-24",
                    "lugarNacimiento": "La Serena",
                    "fechaDefuncion": "",
                    "lugarDefuncion": ""
                },
                "trayectorias": {
                    "trayectoria": [
                        {
                            "tipoParlamentario": "Diputado",
                            "partidoPolitico": "Partido Comunista de Chile",
                            "periodoInicio": 1969,
                            "periodoTermino": 1973,
                            "divisionElectoral": "7ª Agrupación Departamental \"Santiago\", primer distrito"
                        },
                        {
                            "tipoParlamentario": "Diputado",
                            "partidoPolitico": "Partido Comunista de Chile",
                            "periodoInicio": 1965,
                            "periodoTermino": 1969,
                            "divisionElectoral": "7ª Agrupación Departamental \"Santiago\", primer distrito"
                        },
                        {
                            "tipoParlamentario": "Diputado",
                            "partidoPolitico": "Partido Comunista de Chile",
                            "periodoInicio": 1961,
                            "periodoTermino": 1965,
                            "divisionElectoral": "7ª Agrupación Departamental \"Santiago\", primer distrito"
                        },
                        {
                            "tipoParlamentario": "Diputado",
                            "partidoPolitico": "Partido Comunista de Chile",
                            "periodoInicio": 1957,
                            "periodoTermino": 1961,
                            "divisionElectoral": "7ª Agrupación Departamental \"Santiago\", primer distrito"
                        }
                    ]
                },
                "reseniaResumen": "José Luis Cademártori (La Serena, 24 de septiembre de 1930). Ingeniero comercial, académico y político chileno del Partido Comunista. Diputado por cuatro periodos consecutivos entre 1957 y 1973 por la Séptima Agrupación Departamental \"Santiago\", primer distrito.",
                "familiaJuventud": "Nació en La Serena el 24 de septiembre de 1930; hijo de José Cademártori Vaccaro y Stella Invernizzi. Se casó con Xenia Dujisin y tuvieron tres hijos: Yanina, Jean José y Andrés.",
                "estudiosVidaLaboral": "Sus estudios escolares los realizó en un colegio de monjas italianas en Arica, en un establecimiento educacional de sacerdotes en Iquique y en el Patrocinio San José de la ciudad de Santiago. La educación superior la realizó en la Escuela de Economía de la Universidad de Chile donde se tituló de Ingeniero Comercial en 1952 con la memoria de tesis titulada “Las cuentas nacionales: naturales y experiencia”, establecimiento donde posteriormente se desempeñaría como ayudante y profesor. Durante sus estudios conoció a su mujer, Xenia Dujisin, con quien tuvo tres hijos.\n            En el ámbito laboral, durante el segundo gobierno de Carlos Ibáñez del Campo, entre 1952 y 1954, trabajó como asesor del Ministro de Hacienda Juan Bautista Rossetti, incorporándose después al recién creado Ministerio de Minería a cargo de Clodomiro Almeyda. Luego se incorporaría como Jefe de Sección del Departamento de Planificación de la Corporación de Fomento, CORFO, donde se desempeñaría además como dirigente de la Asociación de Empleados entre 1959-1960 y Senador Consejero en 1957.\n            A su regreso a Chile del exilio, trabajó en el Instituto Alejandro Lipschutz, colaboró en medios periodísticos como Le Monde Diplomatique, Rocinante, La Nación y Punto Final, se dedicó a prestar asesorías además de dictar charlas asumiendo una postura crítica del neoliberalismo expresada en sus libros Chile: el modelo neoliberal del 2001 y en 2004. La globalización cuestionada, entre otros trabajos.",
                "trayectoriaPoliticaPublica": "Miembro del Partido Comunista de Chile, integró el Comité Central del mismo, siendo su titular desde el XII Congreso de 1961. En su actuación político-pública también fue llamado por el presidente Salvador Allende para el cargo de ministro de Economía, Fomento y Reconstrucción, puesto que ocupó entre el 5 de julio de 1973 y el 11 de septiembre del mismo año. Preso tres años en la Escuela Militar de Santiago, en la isla Dawson y en Ritoque, siendo deportado al exilio junto a su mujer y dos hijos en noviembre de 1976. Vivió en Venezuela seis años, hizo clases en la Universidad Central de Caracas y se desempeñó como investigador del Centro de Estudios del Desarrollo, además de dedicarse a la organización política de los exiliados. Hasta 1980 formó parte del “Grupo Caracas” integrado por democratacristianos, radicales, socialistas y comunistas, entre ellos Jaime Castillo Velasco y Renán Fuentealba. Después estuvo un año en Cuba y luego en Alemania durante aproximadamente cinco años hasta su regreso a Chile en 1988 semanas antes del Plebiscito de aquel año.",
                "hemiciclos": {
                    "hemiciclo": [
                        {
                            "periodoInicio": 1969,
                            "periodoTermino": 1973,
                            "descripcion": "Reelecto nuevamente diputado por la Agrupación y Distrito mencionados, período 1969-1973; integró la Comisión Permanente de Hacienda."
                        },
                        {
                            "periodoInicio": 1965,
                            "periodoTermino": 1969,
                            "descripcion": "Fue electo nuevamente diputado por la Agrupación y Distrito ya mencionados, período 1965-1969, donde fue miembro de la Comisión Mixta de Presupuesto, 1963 a 1969 y miembro propietario del Comité Parlamentario Comunista entre 1967-1969."
                        }
                    ]
                },
                "bibliografias": {
                    "bibliografia": {
                        "@url": "https://www.bcn.cl/catalogo/detalle_libro?bib=165061&n=1",
                        "nombre": "Globalización, identidad y justicia social",
                        "editorial": "Universidad Arcis",
                        "ano": 2005,
                        "descripcion": "350 páginas",
                        "isbn": "956811453",
                        "disponible": "1"
                    }
                }
            }
]
    }
]

print("Raw input data:")
print(data)
print("Pretty-printed input data:")
print(json.dumps(data, indent=4))

print("Validating the input data using jsonschema:")
for idx, item in enumerate(data):
    try:
        validate(item, schema)
        sys.stdout.write("Record #{}: OK\n".format(idx))
    except jsonschema.exceptions.ValidationError as ve:
        sys.stderr.write("Record #{}: ERROR\n".format(idx))
        sys.stderr.write(str(ve) + "\n")
