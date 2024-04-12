<?php

namespace App\Controller\API;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\PasswordHasher\Hasher\UserPasswordHasherInterface;
use Symfony\Component\HttpFoundation\JsonResponse;
use App\Entity\User;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Component\Security\Core\Exception\BadCredentialsException;

class LoginController extends AbstractController
{
    private $entityManager;

    public function __construct(EntityManagerInterface $entityManager)
    {
        $this->entityManager = $entityManager;
    }
    #[Route('/api_login', name: 'app_api_login')]
    public function login(Request $request, UserPasswordHasherInterface $passwordEncoder): Response
{
    $data = json_decode($request->getContent(), true);

    $email = $data['email'];
    $password = $data['password'];

    $user = $this->entityManager->getRepository(User::class)->findOneBy(['email' => $email]);

    if (!$user) {
        throw new BadCredentialsException('Invalid credentials');
    }

    if (!$passwordEncoder->isPasswordValid($user, $password)) {
        throw new BadCredentialsException('Invalid credentials');
    }

    return new JsonResponse(['status' => 'Logged in successfully'], Response::HTTP_OK);
}
}
