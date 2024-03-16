# Frequently Asked Questions

### How to define an input field as hidden ?
A hidden field can be specified by defining a field as hidden inside the render property. `somefield.render.input` = `hidden` 
```
{
  "form": {
    "fields": [
      {
         "type": "text"
      },
      {
         "render": {
            "input": "hidden"   
         }
      }
    ]
  }
}
```


