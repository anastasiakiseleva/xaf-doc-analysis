---
uid: DevExpress.ExpressApp.FileAttachments.Win.FileTypeFiltersNodesGenerator
name: FileTypeFiltersNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.FileAttachments.Win.IModelFileTypeFilters) node.
syntax:
  content: 'public class FileTypeFiltersNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.FileAttachments.Win.FileTypeFiltersNodesGenerator._members
  altText: FileTypeFiltersNodesGenerator Members
- linkId: "112810"
- linkId: "112781"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of a **BOModel** | **_\<Class\>_** | **FileTypeFilters** node.  It collects [](xref:DevExpress.Persistent.Base.FileTypeFilterAttribute) attributes applied in the code of business classes, and adds corresponding [](xref:DevExpress.ExpressApp.FileAttachments.Win.IModelFileTypeFilter) nodes.

[!include[<FileTypeFilters><FileTypeFiltersNodesGenerator>](~/templates/nodegenerator-example.md)]

This Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.