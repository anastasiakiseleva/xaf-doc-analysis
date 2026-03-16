---
uid: DevExpress.Persistent.BaseImpl.EF.ModelDifferenceAspect.DisplayName
name: DisplayName
type: Property
summary: Gets the [language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo) of the current [](xref:DevExpress.Persistent.BaseImpl.EF.ModelDifferenceAspect) object, or the "(Default language)" text.
syntax:
  content: |-
    [NotMapped]
    public virtual string DisplayName { get; }
  parameters: []
  return:
    type: System.String
    description: A string which specifies the name of the current model difference aspect, or "(Default language)" if the aspect name is empty (if the current aspect specifies culture-neutral model differences).
seealso: []
---
If the [IModelDifferenceAspect.Name](xref:DevExpress.ExpressApp.IModelDifferenceAspect.Name) value is not null or empty, the **DisplayName** property returns this value. Otherwise, the "(Default language)" text is returned. To [localize](xref:113298) this text, use the [IModelLocalizationItem.Value](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem.Value) property of the **Localization** | **Texts** | **DefaultAspectText** node in the [Model Editor](xref:112582).

![ModelDiffs_DefaultAspectText](~/images/modeldiffs_defaultaspecttext118161.png)
