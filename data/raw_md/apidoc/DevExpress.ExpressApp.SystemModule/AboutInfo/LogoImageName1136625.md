---
uid: DevExpress.ExpressApp.SystemModule.AboutInfo.LogoImageName
name: LogoImageName
type: Property
summary: Specifies the name of the image with the logotype of the company that built the application.
syntax:
  content: public string LogoImageName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the name of the image with the logotype of the company that built the application.
seealso:
- linkId: "112792"
---
The [](xref:DevExpress.ExpressApp.Win.SystemModule.AboutInfoController) sets this property to the value of the Application node's **Logo** property, before the [](xref:DevExpress.ExpressApp.SystemModule.AboutInfo) object's Detail View is displayed. You can change this property value at any time before the **AboutInfoController** shows the View. In this instance, your custom image will be displayed.