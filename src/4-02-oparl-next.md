## OParl Next {#oparl-next}

 * OParl basiert nun auf Draft-7 der JSON schema Spefikation. Deswegen müssen alle Objekte nun ein Feld `$schema` enthalten, dass den gleichen Wert wie `type`. Langfristig wollen wir `type` durch `$schema` ersetzen, Clients sollten daher wo möglich `$schema` verwenden.
 * `Person` hat ein Feld `image` erhalten.
 * `Body` kann `mainOrganization` angeben.
 * Für `Organization` kann `memberCount` und `votingMemberCount` angegeben werden.
