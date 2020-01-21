(*
* Name: Ammar Chishti
* Net ID: achishti
* SBU ID: 111717583
*)

(* Part 1 *)

(* 1.1 pow - takes int x and int n and returns x^n.*)
let rec pow x n =
  if n = 0 then 1
  else if n = 1 then x
  else x * pow x (n-1);;

(* 1.2 float_pow - takes float x and int n and returns x^n.*)
let rec float_pow x n =
  if n = 0 then 1.0
  else if n = 1 then x
  else x *. float_pow x (n-1);;

(* 2. Reverse - Reverse a list. *)
let rev list =
  let rec bn ans = function
    | [] -> ans
    | head::tail -> bn (head::ans) tail in
  bn [] list;;


(* 3. Compress - Remove consecutive duplicates from a list.*)
let rec compress = function
    | arg1 :: (arg2 :: _ as t) -> if arg1 = arg2 then compress t else arg1 :: compress t
    | remaining -> remaining;;


(* 4. Cluster - Cluster consecutive duplicates into nested lists.*)
let cluster list =
  let rec ans current amb = function
    | [] -> []
    | [x] -> (x :: current) :: amb
    | a :: (b :: _ as t) ->
      if a = b then ans (a :: current) amb t
      else ans [] ((a :: current) :: amb) t  in
  List.rev (ans [] [] list);;


(* 5. Slice - Slice a list based on two integers from i (inclusive) to j (exclusive) *)
let slice list i k =
    let rec get n = function
      | [] -> []
      | h :: t -> if i > k then [] else if n = 0 then [] else h :: get (n-1) t
    in
    let rec remove n = function
      | [] -> []
      | h :: t as l -> if n = 0 then l else remove (n-1) t
    in
    get (k - i) (remove i list);;


(* Part 2 *)

(*1. Composition - Takes two functions as input, returns their composition as the output.*)
let composition f1 f2 x =
  f1 (f2 x);;

(*2. equiv_on - Takes two functions as input, returns true if the functions f and g have identical behavior on ever element of list*)
let rec equiv_on f1 f2 list =
  match list with
  | [] -> true
  | head::tail -> if (f1 head) = (f2 head) then equiv_on f1 f2 tail
                  else false;;

(*3. pairwisefilter - Takes in a function cmp that compares two elements of a specific T and returns one of them, and a list of elements of the same type T.
* Returns a list that applies cmp while taking two items at a time from lst (else if there is an uneven amount leave the last as is.) *)
let rec pairwisefilter cmp list =
  match list with
  | [] -> []
  | [x] -> [x]
  | head::secondHead::tail -> cmp head secondHead :: pairwisefilter cmp tail;;

(*4. polynomial - Takes in a function cmp that compares two elements of a specific T and returns one of them, and a list of elements of the same type T.
* Returns a list that applies cmp while taking two items at a time from lst (else if there is an uneven amount leave the last as is.) *)
let polynomial lst =
  fun coefficient -> List.fold_left (+) 0 (List.map (fun exponent -> (fst exponent) * pow(snd exponent) coefficient) lst);;

(* Part 3 *)

(*1. Write a function called truth_table, which takes as input a logical expression in two literals, and returns its truth table as a list of tuples.*)

type bool_expr =
  | Lit of string
  | Not of bool_expr
  | And of bool_expr * bool_expr
  | Or of bool_expr * bool_expr

let rec compute a expression_a b expression_b = function
    | Lit x -> if x = a then expression_a
               else if x = b then expression_b
               else failwith "Invalid variable found!"
    | Not e -> not(compute a expression_a b expression_b e)
    | And(e1, e2) -> compute a expression_a b expression_b e1 && compute a expression_a b expression_b e2
    | Or(e1, e2) -> compute a expression_a b expression_b e1 || compute a expression_a b expression_b e2

  let truth_table a b expr =
    [(true,  true,  compute a true  b true  expr);
     (true,  false, compute a true  b false expr);
     (false, true,  compute a false b true  expr);
     (false, false, compute a false b false expr) ];;

(*2. Define a polymorphic type Binary_tree. Each element of the tree must be a Node or be Empty. *)
type 'a binary_tree =
  | Empty
  | Node of 'a * 'a binary_tree * 'a binary_tree;;  (*'a is root value, 'a binary_tree is left and 'a binary_tree is right*)

(*3. Write a function called tree2str to obtain the string representation of a binary tree.*)
let rec tree2str tr =
  match tr with
  | Empty -> ""
  | Node(this_value, Empty, Empty) -> string_of_int this_value
  | Node(root, left, right) -> string_of_int root ^ "(" ^ tree2str left ^ ", " ^ tree2str right ^ ")";;
