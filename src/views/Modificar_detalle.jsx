import React, { Component } from "react";
import {
  Grid,
  Row,
  Col,
  FormGroup,
  ControlLabel,
  FormControl
} from "react-bootstrap";

import { Card } from "components/Card/Card.jsx";
import { FormInputs } from "components/FormInputs/FormInputs.jsx";
import { UserCard } from "components/UserCard/UserCard.jsx";
import Button from "components/CustomButton/CustomButton.jsx";
import axios from "axios";

class Modificar_detalle extends Component {
  state = {
    alumno: [],
    //rut:[],
  };

  
  componentDidMount() {
    const currenturl = window.location.pathname
    const largo = currenturl.length
    const urls = currenturl.slice(19,largo)
    const alumnoRUT = this.props.match.params.alumnoRUT;
    

    axios.get(`http://localhost:8000/alumno/${urls}`).then(res => {
      this.setState({
        alumno: res.data,
        //rut: res.data.rut,
      });

    });
}
  render() {
    return (
      <div className="content">
        <Grid fluid>
          <Row>
            <Col md={8} mdOffset={2}>
              <Card
                title="Modificar datos del alumno"
                content={
                  <form>
                    <FormInputs disabled
                      ncols={["col-md-5", "col-md-7"]}
                      properties={[
                        {
                          label: "RUT",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "123456789-8",
                          value: `${this.state.alumno.rut}`,
                          minlength:"9",
                          maxlength:"10",
                          pattern: "[^a-zA-Z][0-9]{7,8}+-[0-9|Kk]",
                          
                        },
                        {
                          label: "Email",
                          type: "email",
                          bsClass: "form-control",
                          placeholder: "usuario@mail.udp.cl",
                          value: `${this.state.alumno.correo}`,
                          minlength:"15",
                          maxlength:"50",
                          pattern: "[a-zA-z0-9.]+@mail.udp.cl",
                          
                        }
                      ]}
                    />
                    <FormInputs
                      ncols={["col-md-8", "col-md-4"]}
                      properties={[
                        {
                          label: "Nombre y Apellido",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Juanito Perez",
                          value: `${this.state.alumno.nombre}`,
                          minlength:"3",
                          maxlength:"50",
                          pattern: "[a-zA-Z]+",
                          minlength:"4",
                          maxlength:"4", 
                          pattern: "[1][9][6-9][0-9]|[2][0-2][0-9][0-9]",
                          
                        },
                        {
                          label: "Año de Nacimiento",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "1970",  
                          minlength:"4",
                          maxlength:"4", 
                          pattern: "[1][9][6-9][0-9]|[2][0-2][0-9][0-9]",
                          value: `${this.state.alumno.año_nacimiento}`, 
                          
                        },
                        
                      ]}
                    />
                    <FormInputs
                      ncols={["col-md-5", "col-md-3", "col-md-3"]}
                      properties={[
                        
                        {
                          label: "Teléfono",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "56997856443",
                          value: `${this.state.alumno.telefono}`,
                          minlength:"11",
                          maxlength:"11", 
                          pattern: "56[0-9]{9}",
                          
                        },
                        {
                          label: "Año de ingreso",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "2016",
                          value: `${this.state.alumno.año_ingreso}`,
                          minlength:"4",
                          maxlength:"4", 
                          pattern: "[1][9][6-9][0-9]|[2][0-2][0-9][0-9]",
                          
                        },
                        {
                          label: "Semestre de ingreso",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "1er semestre",
                          value: `${this.state.alumno.semestre_ingreso}`,
                          minlength:"1",
                          maxlength:"1", 
                          pattern: "[1|2]",
                          
                        },
                      ]}
                    />
                    <FormInputs
                      ncols={["col-md-7", "col-md-4"]}
                      properties={[
                        
                        {
                          label: "Universidad o carrera de origen (si corresponde)",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "UDP, industrias",
                          value: `${this.state.alumno.carrera_origen}`,
                          minlength:"10",
                          maxlength:"30",
                          pattern: "[a-zA-Z,']+",
                          
                        },
                        {
                          label: "Copia del registro ",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "(link al registro)",
                          value: `${this.state.alumno.copia_registro}`,
                          
                        },
                      ]}
                    />
                    <FormInputs
                      ncols={["col-md-4", "col-md-4"]}
                      properties={[
                        
                        {
                          label: "Fecha del registro",
                          type: "date",
                          bsClass: "form-control",
                          placeholder: "07/07/2020",
                          value: `${this.state.alumno.fecha_registro}`,
                          readonly:"readonly"
                          
                        },
                        {
                          label: "Estado actual",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Rehabilitado",
                          value: `${this.state.alumno.estado_actual}`,
                          minlength:"9",
                          maxlength:"20", 
                          pattern:"[En] [cC][aA][uU][sS][aA][lL]|[eE][Nn] [oO][bB][sS][eE][rR][vV][aA][cC][iI][oO][nN]|[rR][eE][cC][uU][pP][eE][rR][aA][Dd][oO]|[sS][uU][sS][pP][eE][nN][cC][iI][oO][Nn]|[eE][lL][iI][Mm][Aa][cC][iI][oO][nN]|[Rr][eE][nN][uU][Nn][cC][Ii][aA] [Cc][aA][Mm][Bb][iI][Oo] [dD][eE] [Cc][aA][Rr][rR][eE][rR][aA]",
                        },
                      ]}
                    />
                    <Button bsStyle="info" pullRight fill type="submit">
                      Actualizar perfil
                    </Button>
                    <div className="clearfix" />
                  </form>
                }
              />
            </Col>
            
          </Row>
        </Grid>
      </div>
    );
  }
}

export default Modificar_detalle;
  
