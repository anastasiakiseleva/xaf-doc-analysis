---
uid: DevExpress.ExpressApp.Updating.IModelXmlConverter.ConvertXml(DevExpress.ExpressApp.Updating.ConvertXmlParameters)
name: ConvertXml(ConvertXmlParameters)
type: Method
summary: Converts the specified [Application Model](xref:112580) node's differences.
syntax:
  content: void ConvertXml(ConvertXmlParameters parameters)
  parameters:
  - id: parameters
    type: DevExpress.ExpressApp.Updating.ConvertXmlParameters
    description: A [](xref:DevExpress.ExpressApp.Updating.ConvertXmlParameters) object, representing the Application Model node's differences.
seealso: []
---
Support the [](xref:DevExpress.ExpressApp.Updating.IModelXmlConverter) interface in your Module and implement the **ConvertXml** method, to make the required changes in the model differences. This method is invoked for each node customized in differences and takes the **ConvertXmlParameters** object as a parameter. This object provides you with access to the node stored in differences. With this method, you can handle, for instance, changing the type of a certain node.
Refer to the [Convert Application Model Differences](xref:112796) topic to see the example.