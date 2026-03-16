---
uid: DevExpress.ExpressApp.SystemModule.AboutInfo.Copyright
name: Copyright
type: Property
summary: Specifies information about the company's copyright.
syntax:
  content: public string Copyright { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying information about the company's copyright.
seealso: []
---
This property value takes place in the [AboutInfo.AboutInfoString](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.AboutInfoString) property's default value construction. [](xref:DevExpress.ExpressApp.Win.SystemModule.AboutInfoController) sets this property to the value of the Application node's `Copyright` property before it displays the `AboutInfoString` in a UI. You can change this property value at any time before the `AboutInfoController` and `AboutInfoControl` display the information. In this case, XAF displays your custom value.