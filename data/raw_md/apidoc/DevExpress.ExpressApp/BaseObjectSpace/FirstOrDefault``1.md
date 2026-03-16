---
uid: DevExpress.ExpressApp.BaseObjectSpace.FirstOrDefault``1(System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}},System.Boolean)
name: FirstOrDefault<ObjectType>(Expression<Func<ObjectType, Boolean>>, Boolean)
type: Method
summary: Searches for the first object that matches the specified lambda expression. The generic parameter determines the object's type. This method takes uncommitted changes into account.
syntax:
  content: |-
    public virtual ObjectType FirstOrDefault<ObjectType>(Expression<Func<ObjectType, bool>> criteriaExpression, bool inTransaction)
        where ObjectType : class
  parameters:
  - id: criteriaExpression
    type: System.Linq.Expressions.Expression{System.Func{{ObjectType},System.Boolean}}
    description: A lambda expression to search for an object.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if the method takes unsaved changes into account; otherwise, **false**.'
  typeParameters:
  - id: ObjectType
    description: The @System.Type of an object to be returned.
  return:
    type: '{ObjectType}'
    description: The first object that matches the specified lambda expression.
seealso: []
---
This method does nothing and returns `null`, override it in `BaseObjectSpace` descendants.