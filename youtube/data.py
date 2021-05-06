"""Data to keep between HTTP requests (app state)

* selected: list of selected videos
* selectable: list of selectable videos
"""

selected = []
selectable = []

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Django YouTube (version 2)</h1>
    <h2>Selected</h2>
      <ul>
      {selected}
      </ul>
    <h2>Selectable</h2>
      <ul>
      {selectable}
      </ul>
  </body>
</html>
"""

VIDEO = """
      <li>
        <form action='/' method='post'>
          <a href='/{video_id}'>{title}</a>
          <input type='hidden' name='id' value='{id}'>
          <input type='hidden' name='csrfmiddlewaretoken' value='{token}'>
          <input type='hidden' name='{name}' value='True'> 
          <input type='submit' value='{action}'>
        </form>
      </li>
"""

VIDEO_INFO = """
    <a href='/'>Go back</a>
    <h2><a href='{link}'>{title}</a></h2>
    <br><img src={img_url}>
    <p><br><b>channel name: </b><a href='{channel}'>{name}</a></p>
    <p><b>Release date: </b>{date}</p>
    <p><b>Video description: </b><br>
    {description}
    </p>
"""