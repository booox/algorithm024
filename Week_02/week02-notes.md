
# 第2周 第5课 | 哈希表、映射、集合

## 1. 哈希表、映射、集合的实现与特性

### 哈希表（Hash table）

* 哈希表（Hash table），也叫散列表，是根据关键码值（key value）而直接进行访问的数据结构。
    * 它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度
* 这个映射函数叫作散列函数（Hash Function），存放记录的数组叫作哈希表（或散列表）
* 哈希碰撞
* 工程上应用
    * map
    * set


#### Java Hashmap 部分函数的实现

* **isEmpty()**

```java
 279:   public boolean isEmpty()
 280:   {
 281:     return size == 0;
 282:   }
```

* **get(key)**

```java
 295:   public V get(Object key)
 296:   {
 297:     int idx = hash(key);               // 对 key 进行 hash
 298:     HashEntry<K, V> e = buckets[idx];  // 获取 idx 所对应的数据池
 299:     while (e != null)                  // 循环查找 key
 300:       {
 301:         if (equals(key, e.key))        // 如果找到，返回 key 对应的 value
 302:           return e.value;
 303:         e = e.next;                    // 在链表中将 e 移到下一节点
 304:       }
 305:     return null;                       // 若没有找到，返回 null
 306:   }
```
* **pull(key)**

```java
 342:   public V put(K key, V value)
 343:   {
 344:     int idx = hash(key);               // 对 key 进行 hash
 345:     HashEntry<K, V> e = buckets[idx];  // 获取 idx 所对应的数据池
 346: 
 347:     while (e != null)                  // 先检测 key 是否已经存在
 348:       {
 349:         if (equals(key, e.key))
 350:           {
 351:             e.access(); // Must call this for bookkeeping in LinkedHashMap.
 352:         V r = e.value;
 353:             e.value = value;
 354:             return r;
 355:           }
 356:         else
 357:           e = e.next;
 358:       }
 359: 
 360:     // At this point, we know we need to add a new entry.
 361:     modCount++;                       // 执行操作记数加 1
 362:     if (++size > threshold)           // 判断容量是否足够
 363:       {
 364:         rehash();
 365:         // Need a new hash value to suit the bigger table.
 366:         idx = hash(key);
 367:       }
 368: 
 369:     // LinkedHashMap cannot override put(), hence this call.
 370:     addEntry(key, value, idx, true);  // 实现 key 的添加
 371:     return null;
 372:   }
```



