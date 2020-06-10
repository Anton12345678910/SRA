/*!

=========================================================
* Light Bootstrap Dashboard React - v1.3.0
=========================================================

* Product Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/light-bootstrap-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React, { Component } from "react";
import { Tooltip, OverlayTrigger } from "react-bootstrap";
import Checkbox from "components/CustomCheckbox/CustomCheckbox.jsx";
import Radio from "components/CustomRadio/CustomRadio.jsx";
import Button from "components/CustomButton/CustomButton.jsx";

export class Tasks extends Component {
  handleCheckbox = event => {
    const target = event.target;
    console.log(event.target);
    this.setState({
      [target.name]: target.checked
    });
  };
  render() {
    const tasks_title = [
      'Apellido',
      "Rut",
      "Cantidad de asignaturas reprobadas",
      "Periodo",
      'Asignatura reportada'];
    var tasks = [];
    var number;
    for (var i = 0; i < tasks_title.length; i++) {
      number = "radio" + i;
      tasks.push(
        <tr key={i}>
          <td>
            <Radio
              number={number}
              isChecked={i === 1 || i === 0 ? true : false}
            />
          </td>
          <td>{tasks_title[i]}</td>
          <td className="td-actions text-left">
          </td>
        </tr>
      );
    }
    return <tbody>{tasks}</tbody>;
  }
}

export default Tasks;