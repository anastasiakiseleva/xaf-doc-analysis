---
uid: DevExpress.ExpressApp.SystemModule.AboutInfo.ProductName
name: ProductName
type: Property
summary: Specifies the application's title.
syntax:
  content: public string ProductName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the product name.
seealso: []
---
This property value takes place in the [AboutInfo.AboutInfoString](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.AboutInfoString) property's default value construction. [](xref:DevExpress.ExpressApp.Win.SystemModule.AboutInfoController) sets this property to the value of the Application node's `Title` property before it displays the `AboutInfoString` in a UI. You can change this property value at any time before the `AboutInfoController` and `AboutInfoControl` display the information. In this case, XAF displays your custom value.