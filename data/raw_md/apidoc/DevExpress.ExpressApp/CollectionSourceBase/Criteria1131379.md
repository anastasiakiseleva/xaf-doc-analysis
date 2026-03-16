---
uid: DevExpress.ExpressApp.CollectionSourceBase.Criteria
name: Criteria
type: Property
summary: Provides access to the Collection Source's [](xref:DevExpress.Data.Filtering.CriteriaOperator) dictionary that define the way in which the Collection Source's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) is filtered.
syntax:
  content: public LightDictionary<string, CriteriaOperator> Criteria { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.LightDictionary{System.String,DevExpress.Data.Filtering.CriteriaOperator}
    description: A **LightDicationary** of the [](xref:DevExpress.Data.Filtering.CriteriaOperator) objects that define the way in which the Collection Source's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) is filtered.
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.CriteriaApplying
- linkId: DevExpress.ExpressApp.CollectionSourceBase.CriteriaApplied
---
To filter a Collection Source's collection, add the required **CriteriaOperator**s to the **Criteria** dictionary. No additional methods have to be called. The dictionary holds **\<String, CriteriaOperator>** pairs. The **String** contains the description of a criterion and the **CriteriaOperator** denotes the criterion. The **LightDictionary** class implements the **IDictionary** interface. So, you can use its methods and properties - **Add**, **Clear**, **Count**, **Remove** and others.

When the content of the **Criteria** dictionary is changed, the Collection Source's collection is filtered automatically. Two events are executed in the process - the [CollectionSourceBase.CriteriaApplying](xref:DevExpress.ExpressApp.CollectionSourceBase.CriteriaApplying) and [CollectionSourceBase.CriteriaApplied](xref:DevExpress.ExpressApp.CollectionSourceBase.CriteriaApplied). Handle them to receive notifications when the Collection Source's collection is filtered.

[!include[Criteria_SessionMixingException](~/templates/criteria_sessionmixingexception111409.md)]

The following topics contain examples on accessing and manipulating the **Criteria** dictionary:

* [Criteria Property of a List View's Collection Source](xref:112988)
* [How to: Use Criteria Property Editors](xref:113143)

> [!NOTE]
> * [!include[CollectionSourceCriteriaNested](~/templates/collectionsourcecriterianested111748.md)]
> * [!include[CollectionSourceTreelist](~/templates/collectionsourcetreelist111750.md)]