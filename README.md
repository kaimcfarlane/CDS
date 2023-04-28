# Canvas Docking Station (CDS)




<p display='flex' flex-direction='row' justify-content='center'>
 <img width="409" height="700px" alt="Screen Shot 2022-12-31 at 6 12 07 PM" src="https://user-images.githubusercontent.com/87865378/235232578-7e202776-dc6a-4982-b10a-851fd196b0e6.JPG">

  <img width="409" height="700px" alt="Screen Shot 2022-12-31 at 6 12 07 PM" src="https://user-images.githubusercontent.com/87865378/235233172-3ca537f3-6bf1-4447-8cbb-39d3020ae922.JPG">
</p>

<div align='center'>
 <h2>
   The CDS is a tool made for UF students to help keep track of their current UF courses.
  </h2>
  <p>
  The Canvas Docking Station (CDS) is a fixed device consisting of an LCD screen, LED lights, and a button that displays a student's current canvas assignments and grades. Four students, including myself, collaborated on the device's creation, with me solely responsible for developing the backend, which is available in this repository. To accomplish this, I utilized the Canvas API (available at ​​https://canvas.instructure.com/doc/api/) and Python to fetch requests on the user's local machine. Next, I parsed the JSON response and redirected the user to their calendar, where I opened and parsed the .ics file using the iCalendar and vObject Python libraries. Finally, I sent this information through a port to the connected Arduino via pyserial. The Arduino then parsed the data for the LCD screen, displaying different data based on the length of the button press. The CDS is held up by an adaptive stand that can be adjusted and has its own cord, connecting power and data to the computer it is used on.
 </p>
 
</div>
 
 
